#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:08:12 2018

@author: mac
"""

import pymysql

def sqldb():
    try:
        db = pymysql.connect("localhost","root", password,"minipro3");
    except:
        print("error!Please check your password")
    return db

def sqlsearch(keywords):
    db = sqldb()
    cursor = db.cursor()
    sql='SELECT twitter_username FROM image_label WHERE image_label like "%{}%"'.format(keywords)'
    try:
        cursor.excute(sql)
        account=cursor.fetchall()
    except:
        print("error!")
        
    username=[]
    for i in account:
        if i not in username:
            username.append(i)
    print("the label you are searching for are in the following account:")
    if username: 
        print(username)
    else:
        print("there is no account")
        

if __name__ == '__main__':
    db = sqldb()
    cursor = db.cursor()
    sql_1 = 'SELECT twitter_username,image_num FROM twitter_id ORDER BY image_num'
    sql_2 = 'SELECT twitter_username,image_label FROM image_label'
    try:
        cursor.excute(sql_1)
        cursor.excute(sql_2)
        db_num = cursor.fetchall()
        db_label = cursor.fetchall()
    except:
        print("error")
    print("the twitter_id is")
    print(db_num)
    print("the image_label is")
    print(db_label)
    
    keyword = sys.argv[1]
    sqlsearch(keyword)
    
