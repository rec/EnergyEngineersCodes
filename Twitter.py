
# coding: utf-8

# ### Import libraries

# In[1]:

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
import numpy as np

import time
import json

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


# ### Define LED parameters

# In[2]:

LedsPerSide = 8
NumLeds= LedsPerSide*4*2 ##* 4 sides * 2 levels
driver=DriverLPD8806(NumLeds)
led=LEDStrip(driver)


# ### Authentication
# #### (From BrannonDorsey LoopLamp Project)

# In[3]:


consumer_key = "TroyIuC1l3i3laNlwl5mg"
consumer_secret = "qYRSTEHzHhTsL0CBcMnXxjqeY5UQ6U4C0kNvmPSG4K4"
access_token = "1230084602-UtUB4QdlhNkv1aLqrjS3eYoZ96APon5IhjOqBFt"
access_secret = "wscl1nV8gFO4kMhtJy7DjhQKkpJHB1fW5Jzb4RXZq8"
   
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# ### Define flashmode

# In[4]:

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
            
            print ('New Tweet!!')
            
            self.flash(0.5, (np.random.randint(1,255),np.random.randint(1,255),np.random.randint(1,255)))
            with open('twitter_out.json', 'a') as f:  #set output filename here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#trump']) #set hashtag here; 


# In[3]:

np.random.randint(1,255)


# In[ ]:




# In[ ]:



