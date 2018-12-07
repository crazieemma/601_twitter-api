#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:10:46 2018

@author: mac
"""

import tweepy #https://github.com/tweepy/tweepy
from tweepy import OAuthHandler
#import json
import wget
import os
import io
import sys
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pymysql



#Twitter API credentials
consumer_key = ""  #enter the consumer_key
consumer_secret = "" #enter the consumer_secret
access_key = ""   #enter the access_key
access_secret = ""   #enter the access_secret
#
#@classmethod
#def parse(cls, api, raw):
#    status = cls.first_parse(api, raw)
#    setattr(status, 'json', json.dumps(raw))
#    return status
# 
## Status() is the data model for a tweet
#tweepy.models.Status.first_parse = tweepy.models.Status.parse
#tweepy.models.Status.parse = parse
## User() is the data model for a user profil
#tweepy.models.User.first_parse = tweepy.models.User.parse
#tweepy.models.User.parse = parse
## You need to do it for all the models you need

def twitter_api(user_name):

    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)

#Getting the tweets from a user
    api = tweepy.API(auth)
    alltweets = []
    tweets = api.user_timeline(screen_name=user_name, count=20)
    
    alltweets.extend(tweets)
    last_id = alltweets[-1].id-1  #save the id of the last tweets
     

    while (True):
        more_tweets = api.user_timeline(screen_name=user_name,count=200,include_rts=False,exclude_replies=True,max_id=last_id-1)

# There are no more tweets
        if (len(more_tweets) == 0):
            break
        else:
            last_id = more_tweets[-1].id-1
            tweets = tweets + more_tweets
        if(len(tweets)>=10): #you can change the number if you want to download more images
            break

#write tweet objects to JSON
    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")

# Obtaining the full path for the images     
    media_files = set()
    for status in tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
# Download the images
    i=0
    for media_file in media_files:
        wget.download(media_file)
        i=i+1
        print('%d images have been downloaded'%i)
    image_num = i
    print('%d images have been downloaded in total'%image_num)

#connect mysql
    db = pymysql.connect("localhost","root", password,"minipro3");
    cursor = db.cursor()
    sql = """INSERT INTO twitter_id(twitter_username, image_num) VALUES (%s,%s)"""
    try:
        cursor.execute(sql,(user_name,image_num))
        db.commit()
    except:
        db.rollback()

        
# Rename the images
    path='/Users/mac/Desktop/TWITTER/' 
    filelist = os.listdir(path)
    i=1
    total_num = len(filelist) 
    for item in filelist:
        if item.endswith('.jpg'):  
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(path), ''+str(i) + '.jpg')
            try:
                os.rename(src, dst)
                print ('converting %s to %s ...' % (src, dst))
                i = i + 1
            except:
                continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))
    return image_num

if __name__ == '__main__':
    
    account_name=sys.argv[1] 
    image_num =twitter_api(account_name)
    
    client = vision.ImageAnnotatorClient()
# The name of the image file to annotate

    for i in range(1,image_num+1):
        name = str(i)+'.jpg'
        file_name = os.path.join(os.path.dirname(__file__),name)

    # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('labels:')
        label_text = []
        for label in labels: 
            label_text.append(label.description)
            print(label.description)

        label_text_str=str(label_text) 
    #connect mysql
        db = pymysql.connect("localhost","root",password ,"minipro3");
        cursor = db.cursor()
        sql = """INSERT INTO image_label(twitter_username, image_label) VALUES (%s,%s)"""
        try:
            cursor.execute(sql,(account_name,label_text_str))
            db.commit()
        except:
            db.rollback()

        img = Image.open(file_name)
        draw =  ImageDraw.Draw(img)
        newfont=ImageFont.truetype('ubuntu.ttf',12)
        draw.text((0,20),label_text_str,font=newfont)
        img.save(file_name)
    

os.system("ffmpeg -framerate 1/5 -i %d.jpg -c:v libx264 -vf out.mp4")
