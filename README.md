# Project Readme
## Title: 
Correlation between Donald Trump hashtag and the price of the american dollar in Mexiacan pesos

## Authors: 
César Arcos Gonzalez, Saul Armas Gamiño

## Contact information:
César Arcos Gonzalez: racec9999@gmail.com, Saul Armas Gamiño:luasikirfl@gmail.com

## License : 
CC BY-NC

## Introductions: 
Our goal is to find correlation between the amount of tweets with #DonaldTrump and the Usa dollar price in Mexican pesos. We get daily twitter data using the python library named Tweepy and the usa dollar price with Forex-python.


## Installation and execution information:
How to install and run this project on linux
- First, you need to install Tweepy, Forex-python and MySQL:
    - open a terminal and run the next code:
    - pip install tweepy
    - pip install forex-python
    - sudo apt-get install mysql-server mysql-client
       - the system will ask your a password and a new one for the root user of MySQL
    - now, you need create the database and the table to save the data, If you closed the terminal before install mysql, open it again, if it's already opened , write the nexts commands:
    - sudo su
    - MySQL -h localhost -u root -p
    ◦ MySQL  will ask you for the password that you created before when you install the service.
    When you are inside of MySQL, first, you need create a new user, for this, use the next code:
  
		CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
    
- on this command, replace “new user” for the username  you want, and “password” for a secure password.
Then, create a database named “datos”, whit the next command:

	CREATE DATABASE datos;
- on this database, create a table named “tipo_cambio_tweets”,this table will contain the amount of tweets,the value of 1 Usa dollar in mexican pesos and the date of the request, for this use the nexts commands:

	- USE datos;
	- CREATE TABLE tipo_cambio_tweets(date date, tweet int, dollar 	float, primary key(date));

 (or if you want another names, you can write whatever you want, but you will need change the document “db.json” that you will create in a future).Now the database is completed.

Second, you need to install mysql-connector-python:
	pip install mysql-connector-python
In case you get an error, you can find more information about how to install it here: https://www.a2hosting.com.mx/kb/developer-corner/mysql/connecting-to-mysql-using-python

Next, you need create the directories where the resources will be, create a directory on your home page, named “project”, and inside of this, create a directories named “config” and ”graficas”, on “config” create a json document, named “db.json” whit the next data:
	{"user":"your database user","password":"your database password","host":"127.0.0.1","database":"name of your database","raise_on_warnings":true}



In the folder “proyect” put the scripts “collecting_data.py”, ”data_process.py” and “storedb.py”, and the file “twitter_credentials.py”.

You will need change a little details on “storedb.py” and “data_process”, change the variable PATH according to your project.

We upload a json files that you can use to test, only download and put this files on “project”.
To execute first run collecting_data.py this file get the tweets and the usa dollar price and save the information in a json file,now execute storedb.py this script load our json files and save them in the database finally execute data_process.py this script will give you the chart.


## implementation: 
Code : racec9999/distributed-computing

## Diagrams
-Processing data diagram
![dataprocess](https://user-images.githubusercontent.com/60860385/80925163-448b4000-8d53-11ea-9d75-fb1c3dcf8dd6.jpg)
-Information flow diagram (local)
![datafllcoal](https://user-images.githubusercontent.com/60860385/80925223-a64baa00-8d53-11ea-86d4-d5adbcf2b269.jpg)
-Information flow diagram (online) 
![dataflinternet](https://user-images.githubusercontent.com/60860385/80925268-e9a61880-8d53-11ea-8a7a-d05a0fcd7bc2.jpg)
-Logical connections diagram (local)
![logicalconnectionlocal](https://user-images.githubusercontent.com/60860385/80925301-32f66800-8d54-11ea-8e4d-223cae509199.jpg)

-Logical connections diagram (online)


![logicalconectionsinternet](https://user-images.githubusercontent.com/60860385/80925309-473a6500-8d54-11ea-859e-360af1b81bb2.jpg)

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

