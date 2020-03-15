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
To run the file you need to use python and install tweepy ( https://www.tweepy.org/ ) and install forex-python ( https://pypi.org/project/forex-python/ ),set the twitter credentials in a file named twitter_credentials.py

## Introductions: 
we set the principal libraries to get the  twitter data, we did a test with the words Donald Trump and the usd dollar price in mexican pesos

## implementation: 
code : racec9999/distributed-computing/witter_streamer.py

## Results:
we can get 18000 tweets every 15 min, we will analise them to decide which is useful for the proyect. Following we're going to add the tweets to a pandas dataframe and count it.   
price of the dollar at the moment: 21.4188580692


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



## Data source:
- Twitter http://www.tweepy.org/      

- FOrex https://pypi.org/project/forex-python/

