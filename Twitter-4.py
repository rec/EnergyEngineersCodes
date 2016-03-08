
# coding: utf-8

# ### Import libraries

# In[1]:

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
import numpy as np

import time
import json
from datetime import datetime

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


# ### Define LED parameters

# In[2]:

LedsPerSide = 10
NumLeds= LedsPerSide*4*2 ##* 4 sides * 2 levels
driver=DriverLPD8806(NumLeds, ChannelOrder.BRG)
led=LEDStrip(driver)


# ### Authentication 1
# #### (From BrannonDorsey LoopLamp Project)

# In[7]:

#consumer_key = "TroyIuC1l3i3laNlwl5mg"
#consumer_secret = "qYRSTEHzHhTsL0CBcMnXxjqeY5UQ6U4C0kNvmPSG4K4"
#access_token = "1230084602-UtUB4QdlhNkv1aLqrjS3eYoZ96APon5IhjOqBFt"
#access_secret = "wscl1nV8gFO4kMhtJy7DjhQKkpJHB1fW5Jzb4RXZq8"


# ### Authentication 2
# #### (SmartLamp App)

# In[5]:

#consumer_key = "4KxmuenXbg3BEQkw8dr0OQukG"
#consumer_secret = "6oKhNjtiadaCrPEdC6iyo4o8WoWNxghn7mI3VHNDqaSWNdnpPy"
#access_token = "28338904-JhFu09cI0hCcjQ9X6gDOAvrnvuTiuvsFxPCxL0B1x"
#access_secret = "yemTMjMXoZT120Nw4Z4947zB1ADoGVHZLHb3tdLppJNxe"


# ### Authentication 3
# #### (SmartLamp2 App)

# In[3]:

#consumer_key = "dMKVYd1EVI5ac5WcpMwemYcFM"
#consumer_secret = "TY1cahDWwBPN2fg4GeLZ5wvnfBlTLTDPFiWPH9YUxlWeYMEtsZ"
#access_token = "28338904-u7aHX0RrCR8VoM6ONYhjUToCsGJTmtgGq6hKthiVP"
#access_secret = "OOA8YkFnkKCY9xGK0P0gFMimRtzEhKG6sW0ZBBWnnlUYC"


# ### Authentication 4
# #### (SmartLamp3 App)

# In[3]:

consumer_key = "RUmOeWto992y4HqJWKP5XEUlx"
consumer_secret = "i3t2oaaZcatTlMlRlsqaC5dUVNTdFOdnkelJJ2FA71PSAOvUfl"
access_token = "28338904-BCDVUBUIRZCSHJG88phypCMkVPwfnqGV0kHmgpCXH"
access_secret = "Ca9TzkD7jbpleEqcYMFMWXMLXJH7XD9H8QVq3joD7hvQe"


# ### Authentication 5
# #### (SmartLamp4 App)

# In[ ]:

#consumer_key = "TXYjr7ogYQKAR23qFoT7jyiQI"
#consumer_secret = "H3MypqdYnu7A3wIjDiRaxKJXuQj4xuEJtqZtXQEF0ULPKYMDDA"
#access_token = "28338904-bHWBbUtKMftWYX68vvPwbAcULVZtLjrwdL4lk1M5k"
#access_secret = "AP6vzdlBAa5F8mSqa0C6bYkO2qNtqNYwhKXdrQyZjkRkN"


# In[5]:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# ### Define flashmode

# In[6]:

#Streaming API Listner
class MyListener(StreamListener):

    def flash(self, delay, color):
        led.fill(color)
        #print color
        led.update()
        time.sleep(delay)
        
        led.all_off()
        led.update()
        #print delay
        return True

 
    def on_data(self, data):
        try:
            
            self.flash(0.5, (np.random.randint(1,255),np.random.randint(1,255),np.random.randint(1,255)))
            #with open('twitter_out.json', 'a') as f:  #set output filename here
               # f.write(data) return True
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ': someone tweeted #' + hashtag +'!'
            

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


print 'What hashtag would you like to track?'
hashtag = raw_input('Enter here: #')

#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#trump']) #set hashtag here; 


# In[ ]:

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#'+hashtag]) #set hashtag here; 


# In[ ]:



