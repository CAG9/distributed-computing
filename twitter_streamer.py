from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import twitter_credentials
from forex_python.converter import CurrencyRates

class StdOutListener(StreamListener):#inherit from stream listener
    
    def on_data(self,data): #listening for tweets
        print(data)
        return True
    
    def on_error(self,status):
        print(status)
        
if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
    arr = []
    stream = Stream(auth,listener)
    c = CurrencyRates()
    print(c.get_rate('USD', 'MXN'))
    stream.filter(track=['donald trump'])

#license Attribution-NonCommercial 4.0 International
#contac:
#César Arcos Gonzalez: racec9999@gmail.com
#Saul Armas Gamiño:luasikirfl@gmail.com
