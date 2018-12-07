#!/usr/bin/python3
 
import pymysql
 
# open the connection of database
db = pymysql.connect("localhost","root","","minipro3" )
 
cursor = db.cursor()
# drop the table if exist
cursor.execute("DROP TABLE IF EXISTS twitter_id")
cursor.execute("DROP TABLE IF EXISTS image_label")
 
# create the tables
sql_table1 = """CREATE TABLE twitter_id(   
                id INT NOT NULL AUTO_INCREMENT,  
                twitter_username VARCHAR(45),  
                image_num INT NOT NULL,  
                PRIMARY KEY (id) ); """
sql_table2 = """CREATE TABLE image_label(   
                id INT NOT NULL AUTO_INCREMENT,  
                twitter_username VARCHAR(45),  
                image_label VARCHAR(1000),   
                PRIMARY KEY(id) );"""
 
cursor.execute(sql_table1)
cursor.execute(sql_table2)
 
# close the connection
db.close()
