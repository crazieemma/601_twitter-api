# 601—mini project
## twitter-api
### Build a library (preferable in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.

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

## ffmpeg.sh  
  Use FFMPEG to convert images to videos

## google-cloud-vision.py  
  Get Google Vision analysis to describe the content  
  Get labels on the images

## whole_twitter_api.py  
  The whole code for the project,after setting the envinorment,you can run this python file and you can get a video with labeled images.
  
## Environment setting  
  pip install wget  
  pip install Pillow  
  Download the "ubuntu.ttf" and put it into the same folder of the 'goole-cloud-vision.py'file
  
  
  # 601-mini project3--DATABASE
      * MySQL ---- branch [sql_database](https://github.com/crazieemma/601_twitter-api/tree/sql_database)
      * MongoDB ---- branch [database_mongoDB](https://github.com/crazieemma/601_twitter-api/tree/database_mongoDB)
