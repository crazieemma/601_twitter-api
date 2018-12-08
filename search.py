#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:15:56 2018

@author: mac
"""

import pymongo
import sys


def search_id(keywords):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["minipro3_mon"]
    dblist = myclient.list_database_names()
    if "minipro3_mon" in dblist:
        print("The database exists.")
    mycol = mydb["image_label"]
    twitter_account=[]
    for x in mycol.find({},{ "image_label": keyword }):
        if x['twitter_id'] not in twitter_account:
            twitter_account.append(x['twitter_id'])
    if twitter_account:
        print(twitter_account)
    else:
        print('There is no account that fit you search')
    return twitter_account

def search_num(num):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["minipro3_mon"]
    dblist = myclient.list_database_names()
    if "minipro3_mon" in dblist:
        print("The database exists.")
    mycol = mydb["twitter_id"]
    account_num = []
    for x in mycol.find({},{"image_num": num }):
        if x['twitter_id'] not in account_num:
            account_num.append(x['twitter_id'])
    if twitter_account:
        print(account_num)
    else:
        print('There is no account that fit you search')
    return account_num

if __name__ == '__main__':
    
    keywords=sys.argv[1]
    search_id(keywords)
    num = sys.argv[2]
    search_num(num)
       
        
