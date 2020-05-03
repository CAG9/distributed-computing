from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
from forex_python.converter import CurrencyRates
import twitter_credentials
import tweepy
import pandas as pd
import os
import datetime
from datetime import datetime
import json
from datetime import timedelta



class StdOutListener(StreamListener):#inherit from stream listener

    def on_data(self,data): #listening for tweets
        print(data)
        return True

    def on_error(self,status):
        print(status)



if __name__ == "__main__":

    MAX_TWEETS = 5000000000000000000000
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit = True)

    arr = []


    stream = Stream(auth,listener)
    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = datetime.strftime(datetime.now() - timedelta(1),'%Y-%m-%d')

    
    tweets = 0
    #'#DonaldTrump since:2020-04-27 until:2020-04-28'
    Tdate = '#DonaldTrump since:'+yesterday+' until:'+today
    for tweet in tweepy.Cursor(api.search, q=Tdate, count=100).items(MAX_TWEETS):
        tweets+=1
    
    c = CurrencyRates()   
    dolar_price = c.get_rate('USD', 'MXN')
    print("today", today)
    print("Dolar price: "+ str(dolar_price))
    print("Total tweets: " + str(tweets))
    
    save_file = {
        'date': today,
        'tweet': tweets,
        'dolar': dolar_price
        }
    
    
    with open('tweet_collector.json','w') as json_file:
        json.dump(save_file,json_file)
