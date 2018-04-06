#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modified on Fri 06 April 2018
@author: OstermannFO
twitterdatacollection_streaming.py:
    access TwitterStreamingAPI
    write Tweets as JSON objects in text file

this is a version for python 3
"""

import twitter
import json
import time

# set query parameters
TRACK = '' #Comma-separated list of terms
LOCATIONS = '' #bounding box, South-West corner (LONLAT) to North-East corner (LONLAT)

# set path to output files
OUTPUT_PATH = ''

# add authentification details (from Twitter's application page - https://apps.twitter.com/
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

def oauth_login():
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


def save_json(filename, data):
    with open('{}{}.txt'.format(OUTPUT_PATH, filename),
                 'a') as f:
        f.write(json.dumps(data, ensure_ascii=False).encode('utf-8')+'\n')


def main():
    twitter_api = oauth_login()
    filename = "" + time.strftime("%Y%m%d-%H%M%S")  #Advice: fill in keywords to be place in front of the timestamp
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
    twitter_tweets = twitter_stream.statuses.filter(track=TRACK,
                                                   locations=LOCATIONS)
    for tweet in twitter_tweets:
        save_json(filename, tweet)

if __name__=="__main__":
    main()
