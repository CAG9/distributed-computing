# Trumpy
Correlation between Donald Trump hashtag and the price of the american dollar in Mexican pesos

## Authors: 
- Cesar Arcos-Gonzalez: racec9999@gmail.com
- Saul Armas-Gamiño: luasikirfl@gmail.com

## License : 
CC BY-NC

## Introduction: 
Our goal is to find correlation between the amount of tweets with #DonaldTrump and the Usa dollar price in Mexican pesos, to see if the decentralization of the currencies is the future. We get daily twitter data using the python library named Tweepy and the usa dollar price with Forex-python.

## Requirements
First, you need to install Tweepy, Forex-python and MySQL, this projects run on linux.
* pip install tweepy
    * Tweepy require credentials you can get it here https://developer.twitter.com/en
* pip install forex-python
* sudo apt-get install mysql-server mysql-client
    
## Installation
Clone this repository and change the file "conf_init.py" with your own path, then you need to create the database and the table to save the data, write the nexts commands on a terminal:
- sudo su
- MySQL -h localhost -u root -p
	
◦ MySQL  will ask you for the password that you created before when you installed.
On a MySQL terminal,you need to create a new user, use the next command:
  
<pre><code>CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';</code></pre>
    
- Replace “new user” for your username, and “password” for your password.
Now, create a database named “datos”, whit the next command:

<pre><code>CREATE DATABASE datos;</code></pre>

- Create a new table named “tipo_cambio_tweets”,this table will contain the amount of tweets, the value of 1 Usa dollar in mexican pesos and the date of the request, use the following commands:
<pre><code>Use datos</code></pre>
<pre><code>CREATE TABLE tipo_cambio_tweets(date date, tweet int, dollar float, primary key(date));</code></pre>

 (you can write whatever name for you table,but you will change the document “storedb.py”).Now the database is completed.

You need to edit db.json with your own data

	{"user":"User","password":"password","host":"127.0.0.1","database":"database","raise_on_warnings":true}



Change the script “twitter_credentials.py” with your credentials.



## Run 
Open a terminal and run sequentially the following commands:
##you need to be located on te directory "project"
- python3 conf_init.py 
- python3 collecting_data.py
- python3 storedb.py
- python3 data_process.py



## General objectives:
- Get amount of tweets
- Get the daily usa dollar price in mexican pesos
- Find correlations between amout of tweets and usa dollar price 
- Show  the correlation with a chart



## Results:
We can get a  pair of charts that show two lines, dollar to mexican pesos and the amount of tweets with the hashtag:#DonaldTrump
the x labels are the specific dates of our amount of tweets and dollar,an illustrative overview. 
![picture](https://user-images.githubusercontent.com/60860385/80922946-063b5400-8d46-11ea-8c93-3f2ac38ff3b7.png)

## Web Page
You can watch our work here:http://www.gicc.unam.mx/blog/trumpy/
![index](https://user-images.githubusercontent.com/60860385/87733612-e5f03280-c795-11ea-84a1-59c527cfcd42.jpeg)

## Conclusion
We can watch a correlation the 06/30/2020 when the value reach the 10000+ tweets, the dollar increase its value. For such things as this, the Decentralization is the future.

## Software tools:
- Tweepy
- Python
- Forex-python

## Diagrams

-Processing data diagram

![dataprocess](https://user-images.githubusercontent.com/60860385/80925163-448b4000-8d53-11ea-9d75-fb1c3dcf8dd6.jpg)

-Information flow diagram

![dataflinternet](https://user-images.githubusercontent.com/60860385/80925268-e9a61880-8d53-11ea-8a7a-d05a0fcd7bc2.jpg)

-Logical connections diagram 

![logicalconectionsinternet](https://user-images.githubusercontent.com/60860385/80925309-473a6500-8d54-11ea-859e-360af1b81bb2.jpg)

## Bibliography:
- Tweepy http://www.tweepy.org/      
- Forex-python https://pypi.org/project/forex-python/

