# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
from tweepy import OAuthHandler
import json
import wget


#Twitter API credentials
consumer_key = "7uDvEIWVgvxIOXwBWdAJ7UDfZ"
consumer_secret = "nVrHW3yl9MF3BaAv2pixDIyTs7xUJcLncKOEsi55TKA5CaWjUN"
access_key = "1039191468932558849-SJAeYD55KMhFkQSTgjBBk9z1KveKbx"
access_secret = "Q8hdIVLKIJUE6azwAUVpYWNGVhTdij8f4KUbrPcgb0FTJ"


auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@Cristiano',
                           count=200, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name='@Cristiano',
                                    count=200,include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        ast_id = more_tweets[-1].id-1
        tweets = tweets + more_tweets
      
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
   
for media_file in media_files:
    wget.download(media_file)
