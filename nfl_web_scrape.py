
from bs4 import BeautifulSoup
import urllib.request
from pprint import pprint
import asyncio
import aiohttp
import json

@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    body = (yield from response.text())
    return body


loop = asyncio.get_event_loop()
sem = asyncio.Semaphore(5)

def process_split_row(dic, team_stats, names, row_num, col_num):
    for i, stat in enumerate(team_stats[row_num].contents[col_num].text.
                             split('-')):
        dic[names[i]] = int(stat)

@asyncio.coroutine
def process_game(game_url, row_index, week, home_pts, road_pts):
    print('processing row %i' % row_index)
    with (yield from sem):
        page = yield from get(url, compress=True)
    game = BeautifulSoup(page, "lxml")
    team_stats = game.find(
        "table", id="team_stats").find_all("tr", recursive=False)
    game_dict = {}
    game_dict['row'] = row_index
    game_dict['week'] = week
    game_dict['home'] = {}
    game_dict['away'] = {}
    for loc, col in [('away', 1), ('home', 2)]:
        loc_dict = game_dict[loc]
        if loc == 'home':
            loc_dict['pts'] = home_pts
        else:
            loc_dict['pts'] = road_pts
        loc_dict['name'] = team_stats[0].contents[col].text
        loc_dict['first_downs'] = int(team_stats[1].contents[col].text)
        loc_dict['turnovers'] = int(team_stats[8].contents[col].text)
        if ':' in team_stats[12].contents[col].text:
            time_of_pos = team_stats[12].contents[col].text.split(':')
        elif ':' in team_stats[13].contents[col].text:
            time_of_pos = team_stats[13].contents[col].text.split(':')
        loc_dict['time_of_pos'] = 60 * int(time_of_pos[0]) + int(
            time_of_pos[1])
        split_stat_names = []
        split_stat_names.append(['rush_att', 'rush_yds', 'rush_tds'])
        split_stat_names.append(['pass_comp', 'pass_att', 'pass_yds',
                                 'pass_td', 'pass_int'])
        split_stat_names.append(['sacked', 'sacked_yds'])
        split_stat_names.append(['fum', 'fum_lost'])
        split_stat_names.append(['penalties', 'penalties_yds'])
        split_stat_names.append(['third_down_conv', 'third_down_att'])
        split_stat_names.append(['fourth_down_conv', 'fourth_down_att'])
        split_stat_rows = [2, 3, 4, 7, 9, 10, 11]
        for names, row in zip(split_stat_names, split_stat_rows):
            process_split_row(loc_dict, team_stats, names, row, col)
    return game_dict

BASE_URL = 'http://www.pro-football-reference.com'
years = range(2010, 2016)
game_db = {}

for year in years:
    print('Processing year %i...' % year)
    tasks = []
    req_url = BASE_URL + '/years/%s/games.htm' % year
    with urllib.request.urlopen(req_url) as url:
        r = url.read()
    soup = BeautifulSoup(r, "lxml")

    table = soup.find("div", class_="table_container").find("tbody")

    rows = table.find_all("tr")
    for i, row in enumerate(rows):
        cells = row.find_all(recursive=False)
        if 'thead' in row['class'] or cells[3].find("a") is None:
            continue
        week = cells[0].text
        date = cells[2].text
        road_win = int('@' in cells[5])
        home_pts = int(cells[7 + road_win].text)
        road_pts = int(cells[8 - road_win].text)
        game_url = BASE_URL + cells[3].find("a")['href']
        tasks.append(process_game(game_url, i, week, home_pts, road_pts))

    games = loop.run_until_complete(asyncio.gather(*tasks))
    game_db[year] = games

with open('output.json', 'w') as outfile:
    json.dump(game_db, outfile)
loop.close()
