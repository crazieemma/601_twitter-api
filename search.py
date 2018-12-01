#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:15:56 2018

@author: mac
"""

import pymongo
import sys

def mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["minipro3_mon"]
    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")
    mycol = mydb["image_num"]
    return mycol

def search(keywords):
    mycol = mongo()
    account_num=[]
    for x in mycol.find({},{"image_label": keywords }):
        if x['twitter_id'] not in account_num:
            account_num.append(x['twitter_id'])
    
    print(account_num)
    
if __name__ == '__main__':
    mycol=mongo()
    keywords=sys.argv[1]
    search(keywords)
       
        
