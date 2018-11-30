CREATE DATABASE minipro3;

CREATE TABLE twitter_id( 
id INT NOT NULL AUTO_INCREMENT, 
twitter_username VARCHAR(45), 
image_num INT NOT NULL,
PRIMARY KEY (id) 
);

CREATE TABLE image_label( 
id INT NOT NULL AUTO_INCREMENT,
twitter_username VARCHAR(45),
image_label VARCHAR(1000), 
PRIMARY KEY(id) 
);
