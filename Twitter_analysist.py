'''
Due to changes in X (Formerly Twitter)
This is unable to pull tweets from free tier and require payment to access anything
'''

import tweepy
import twit_confi
from textblob import TextBlob

consumer_key = twit_confi.CK
consumer_secret = twit_confi.CS

access_token = twit_confi.AT
access_token_secret = twit_confi.ATS

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for tweet in api.search_tweets(q="corgi", lang="en"):
    print(tweet.text)
    analysist = TextBlob(tweet.text)
    print(analysist.sentiment)