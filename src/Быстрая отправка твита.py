﻿import tweepy
import clipboard

consumer_key = "----------"
consumer_secret = "----------"
access_key="----------"
access_secret="----------"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

text = clipboard.get()
if len(text)<=140 and len(text)>0:
    api.update_status(text,1)