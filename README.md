# Project Readme
## Title: 
Correlation between tweets with the word donald trump and the price of the american dollar

## Authors: 
César Arcos Gonzalez, Saul Armas Gamiño

## Contact information:
César Arcos Gonzalez: racec9999@gmail.com, Saul Armas Gamiño:luasikirfl@gmail.com

## License : 
CC BY-NC

## Installation and execution information:
how to install and run this project
- First, you need to install MySQL:
    - open a terminal and run the next code:
    - sudo apt-get install mysql-server mysql-client
       - the system will ask your password, and before a new password for the root user of MySQL
    - now, you need create the database and the table to save the data, If you closed the terminal before install mysql, open it again, if its already open a terminal, put the next code:
    
          - sudo su
          - MySQL -h localhost -u root -p
        ◦ MySQL  will ask you for the password that you create when you install the service.
	When you are inside of MySQL, first, you need create a new user, for this, use the next code:
  
		CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
    
- on this code, replace “new user” for the name that you want, and 	“password” for a real password.
Next, create a database named “datos”, whit the next code:

	CREATE DATABASE datos;
- on this database, create a table named “tipo_cambio_tweets”,this table will contain the number of tweets,the value of 1 dollar in mexican pesos,and the date of the request,for this use the next code:

	- USE datos;
	- CREATE TABLE tipo_cambio_tweets(date date, tweet int, dollar 	float, primary key(date));

 (or if you want another names, you can put whatever you want, but you will need change the document “db.json” that you will create in a future).before this the database will be complete.

Second, you need install mysql-connector-python:
	pip install mysql-connector-python
if you get an error, you can find more information about how install this on: https://www.a2hosting.com.mx/kb/developer-corner/mysql/connecting-to-mysql-using-python

Next, you need create the directories when the resources will be, create a directory on your home page, named “project”, and inside of this, create a directories named “config” and ”graficas”, on “config” create a json document, named “db.json” whit the next data:
	{"user":"usuario","password":"12345","host":"127.0.0.1","database":"datos","raise_on_warnings":true}

Here, replace “usuario” whit the name of the user that you created, change “12345” for the password for the user, and if you don use “datos” for the name of your database, change “datos” for the name that you use.

On the carpet “proyect” put the scripts “collecting_data.py”, ”data_process.py” and “storedb.py”, and the file “twitter_credentials.py”.

You will need change a little details on “storedb.py” and “data_process”, change the variable PATH according to your project.

We upload a json files that you can use to test, only download and put this files on “project” 
## Introductions: 
We set the principal libraries to get the  twitter data, we did a test with the words Donald Trump and the usd dollar price in mexican pesos

## implementation: 
Code : racec9999/distributed-computing/witter_streamer.py

## Results:
We can get a chart that show two lines,dollar to mexican pesos and the amount of tweets with the hashtag:#DonaldTrump
the x labels are the specific dates of our amount of tweets and dollar,an illustrative overview. 
![picture](https://user-images.githubusercontent.com/60860385/80922946-063b5400-8d46-11ea-8c93-3f2ac38ff3b7.png)


## Project definition:
We are going to track the count of tweets countains Donald Trump words in a day. with that data we are going to try to find a correlation between Donald Trump count tweets with the usd dollar in mexcan pesos.

## General objectives:
- Get the twitter streaming 
- Counts  daily Donald Trump words tweets
- Get the daily usd dollar price in mexican pesos
- Find correlations between tweets count and usd dollar price
- Show  the correlation with a graph

## Software tools:
- Tweepy
- Python
- Forex-python



## Bibliography:
- Tweepy http://www.tweepy.org/      
- Forex-python https://pypi.org/project/forex-python/

