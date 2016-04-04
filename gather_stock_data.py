"""This module contains a script to get high granularity stock data for every
stock in the SP500, and store it in a pandas DataFrame
"""

import csv
import os
import datetime
import urllib
import pandas as pd

curr_dir = os.path.dirname(os.path.realpath(__file__))
GOOGLE_BASE_URL = "http://www.google.com/finance/getprices"

def read_SP_500():
    with open(os.path.join(curr_dir, 'sp500.csv'), 'rb') as f:
        reader = csv.reader(f)
        return list(reader)[0]

def stock_data(ticker, d=10, i=60):
    """Returns a dataframe with the last d days of stock data with an interval
    of i seconds (min 60)
    """
    rows = []
    p = {'i': i, 'p': '%id' % d, 'f': 'd,o,h,l,c,v', 'q': ticker}
    params = urllib.urlencode(p)
    url_string = GOOGLE_BASE_URL + "?" + params
    csv_opened = urllib.urlopen(url_string).readlines()
    for line in range(7, len(csv_opened)):
        if csv_opened[line].count(',') != 5:
            # print 'LESS THAT 5 COMMAS on line %i: %s' \
            #     % (line, csv_opened[line].strip())
            continue
        offset, close, high, low, open_, volume = csv_opened[line].strip()\
            .split(',')
        if offset[0] == 'a':
            day = float(offset[1:])
            offset = 0.0
        else:
            offset = float(offset)
        open_, high, low, close = [float(x) for x in [open_, high, low, close]]
        dt = str(datetime.datetime.fromtimestamp(day+(
                 i*offset)))
        rows.append([ticker, dt, open_, high, low, close, volume])
    df = pd.DataFrame(rows, columns=['ticker', 'datetime', 'close', 'high',
                      'low', 'open', 'volume'])
    return df

def sp_data(d=10, i=60):
    """Returns a dataframe with the last d days of stock data with an interval
    of i seconds (min 60) for every stock in the SP500
    """
    sp_tickers = read_SP_500()
    df = pd.DataFrame()
    for ticker in sp_tickers:
        print 'Querying google for %s' % ticker
        s = stock_data(ticker, d=d, i=i)
        df = pd.concat([df, s], ignore_index=True)
    return df

print sp_data()
