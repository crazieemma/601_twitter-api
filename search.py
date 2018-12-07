#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:08:12 2018

@author: mac
"""

import pymysql
import sys

def sql_db():
    try:
        db = pymysql.connect("localhost","root", password,"minipro3");
    except:
        print("error!Please check your informations")
    return db

def search_label(keywords):
    db = sql_db()
    cursor = db.cursor()
    sql='SELECT twitter_username FROM image_label WHERE image_label like "%{}%"'.format(keywords)
    try:
        cursor.excute(sql)
        account_id=cursor.fetchall()
    except:
        print("error!")
        
    username=[]
    for i in account_id:
        if i not in username:
            username.append(i)
    print("the label you are searching for are in the following account:")
    if username: 
        print(username)
    else:
        print("there is no account that fit your search")
        
def search_num(num):
    db = sql_db()
    cursor = db.cursor()
    sql = "SELECT twitter_username FROM twitter_id WHERE image_num > %s"%(num)
    try:
        cursor.excute(sql)
        account_id=cursor.fetchall()
    except:
        print("error!")
    twitter_id=[]
    for i in account_id:
        if i not in username:
            username.append(i)
    print("the user you are searching for are: ")
    if twitter_id: 
        print(twitter_id)
    else:
        print("there is no account that fit your search")
        

if __name__ == '__main__':
    '''
    db = sql_db()
    cursor = db.cursor()
    sql= "SELECT twitter_username FROM twitter_id ORDER BY image_num"
    try:
        cursor.excute(sql_1)
        db_num = cursor.fetchall()
    except:
        print("error")
        
    print("the twitter_id is")
    print(db_num)
    '''
    
    keyword = sys.argv[1]
    num = sys.argv[2]
    search_label(keyword)
    search_num(num)
    
