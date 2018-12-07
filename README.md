# 601—mini project
## Twitter-API
### Build a library (preferable in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.
## Database
### Store all relevant information for everytime a user uses your application
### Search for certain words and retrieve which user/session that has this work in it. 
### Collective statistics about overall usage of the system. 


# Content：

## twitter.py----Twitter API to access the twitter content  
1.you need to create a twitter app,visit this website:https://developer.twitter.com  
2.sign in with your twitter account and create a New Application  
3.Create Your Access Token.Once you’ve done this, make a note of your Twitter API credentials  
Consumer_Key = “xxxxxxxxxxxx”   
Consumer_Secret  = “xxxxxxxxxxxxx”  
Access_Token  = “xxxxxxxxxxxx”  
Access_Secret = "xxxxxxxxxxxxx"  
4.put your api credentials in the twitter.py  
5.run twitter.py,you will see"Please input the twitter you want to download:",input the twitter account that you want to downlad image from,and you will get the images.

## 

## Environment setting  
  pip install wget  
  pip install Pillow  
  Download the "ubuntu.ttf" and put it into the same folder of the 'goole-cloud-vision.py'file

## DATABESE
### Install SQl
```
$ git clone https://github.com/PyMySQL/PyMySQL
$ cd PyMySQL/
$ python3 setup.py install
```

### Create SQL database. 
  You can run the following code in terminal to go into the database and create the Table,or you can just run the [sql_database.py](https://github.com/crazieemma/601_twitter-api/blob/sql_database/sql_database.py)
```
  alias mysql=/usr/local/mysql/bin/mysql
  alias mysqladmin=/usr/local/mysql/bin/mysqladmin
  mysql -u root -p
```
```
  CREATE TABLE twitter_id(   
  id INT NOT NULL AUTO_INCREMENT,  
  twitter_username VARCHAR(45),  
  image_num INT NOT NULL,  
  PRIMARY KEY (id) ); 
```
```
  CREATE TABLE image_label(   
  id INT NOT NULL AUTO_INCREMENT,  
  twitter_username VARCHAR(45),  
  image_label VARCHAR(1000),   
  PRIMARY KEY(id) );
```

### Search Information
   You can run the [search.py](https://github.com/crazieemma/601_twitter-api/blob/sql_database/search.py) to get the twitter_id depending on your input label.And you can get the twitter_id whose image_num more than the number you input.
