import os
import tweepy
import pprint
import csv

"""
    Query the user for their consumer key/secret
    then attempt to fetch a valid access token.
"""


class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        tweepy.StreamListener.__init__(self)
        self.counter = 0
        self.tweets = []
        self.handle = csv.writer(open('test.csv', 'a'))

    def on_status(self, status):
        print status.text

        # self.counter += 1
        # print self.counter

        # try: 
        #     tweet = [status.created_at, status.timestamp_ms, status.text, status.place.country_code, 
        #              status.user.name, status.user.followers_count, status.user.verified,
        #              status.user.statuses_count]

        #     self.tweets.append([unicode(el).encode("utf-8") for el in tweet])

        # except Exception, e:
        #     print e 

        # if self.counter % 100 == 0:
        #     self.handle.writerows(self.tweets)
        #     self.tweets = []

if __name__ == "__main__":

    access_key = os.getenv("TWITTER_ACCESS_KEY")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")

    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    while True:
        try:
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
            myStream.filter(track=['apple'])
        except Exception, e:
            continue