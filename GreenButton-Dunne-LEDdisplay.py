
# coding: utf-8

# ### Import libraries

# In[1]:

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.json import json_normalize

import time

from datetime import datetime
from dateutil import tz

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
import bibliopixel.colors as colors


# In[2]:

## read data
df_total = pd.read_pickle('All_meters_concat')
df_new = pd.read_pickle('Dunne_Daily_Average')


# ### Generating color scale

# In[3]:

red = 0
green = 255
stepSize = 50
color_gn_rd = []
color_gn_rd.append((red, green, 0)) 


# In[4]:

while(red < 255): ## start with green and increase red
    red += stepSize;
    if(red > 245):
        red = 255; 
    color_gn_rd.append((red, green, 0))

while(green > 0): ## start with red + green and decrease green
    green -= stepSize;
    if(green < 6):
        green = 0; 
    color_gn_rd.append((red, green, 0)); 
    
total_colors = len(color_gn_rd)


# ### Setting up LEDs

# In[5]:

LedsPerSide = 10
numLeds= LedsPerSide*4*2 ##x/side * 4 sides * 2 levels
driver=DriverLPD8806(numLeds, ChannelOrder.BRG)
led=LEDStrip(driver)


# ### Defining Flashing modes

# In[6]:

def led_set(start_position, numLEDs, color): ## Fills the colors
    led.fill(color, start=start_position,end=start_position+numLEDs)
    led.update()
    #print color
    return

def led_pulse(start_position, numLEDs, color):
    ## Step-up intensity by 10% increments, then step down by the same every 0.1 seconds. total time = 4 sec
    
    intensity = np.arange(0,1.1,0.1) 

    for i in intensity:
        color_new = (int(color[0]*i),int(color[1]*i),int(color[2]*i)) 
        # There is probably a more elegant way to do this.. 
        #print color_new
        led.fill(color_new, start=start_position,end=start_position+numLEDs)
        led.update()
        time.sleep(0.1)

    for i in reversed(intensity):
        color_new = (int(color[0]*i),int(color[1]*i),int(color[2]*i)) 
        #print color_new
        led.fill(color_new, start=start_position,end=start_position+numLEDs)
        led.update()
        time.sleep(0.1)        


# ### Calculate Average Data

# In[7]:

#Added by Month

df_total['Month'] = pd.DatetimeIndex(df_total['time_stamp']).month
df_Monthlygroup = df_total.groupby('Month')
df_MonthlyAverage = df_Monthlygroup['value'].sum()

#Added by Day

df_total['Date'] = pd.DatetimeIndex(df_total['time_stamp']).date
df_Dailygroup = df_total.groupby('Date')
df_DailyAverage = df_Dailygroup['value'].sum()
df_RollingMean = pd.rolling_mean(df_DailyAverage, 30)


# ### Displaying Daily Total Values for the entire year of data

# In[8]:

def yearly_data():
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'
        max_value = df_DailyAverage.max()
        ScalingSteps = (max_value + 0.1)/(total_colors)
        for item in df_DailyAverage.iteritems():
            print 'Date: ', item[0]
            print 'Average use: ', item [1]
            color_index = int(item[1]/ScalingSteps)
            # print color_index
            color = color_gn_rd[color_index]
            led_set(0, 80, color)


# ### Displaying Daily Energy Usage on Bottom with last 30 days' average on Top

# In[9]:

def daily_vs_past30days():
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'
        max_value = df_DailyAverage.max()
        ScalingSteps = (max_value + 0.1)/total_colors
        count = 0
        for item in df_DailyAverage.iteritems():
            print 'Date: ', item[0]
            print 'Total use: ', item [1]
            color_index = int(item[1]/ScalingSteps)

            # print color_index
            color = color_gn_rd[color_index]
            led_set(0, 40, color)

            print 'Last 30 days average: ', df_RollingMean[count]
            try:
                color_index = int(df_RollingMean[count]/ScalingSteps)
                color = color_gn_rd[color_index]
                led_set(40, 80, color)

            except:
                color = (0,0,0)
                led_set(40, 80, color)

            count = count + 1

    


# ### Displaying 1 Week's Energy Use (res: every half-hour )

# In[10]:

def OneWeek_data():
    date = pd.DatetimeIndex(df_1Week.index).date[1]
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'

        for item in df_1Week.iteritems():
            ts = item[0]

            type(ts.date)
            if(date != time.strftime("%Y-%m-%d",  time.strptime(str(ts), "%Y-%m-%d %H:%M:%S"))):
                led_pulse(0, 80, (0,0,255))

            print 'Time: ', item[0]
            print 'Electricity Usage: ', item [1]
            color_index = int((item[1])/ScalingSteps)

            print color_index
            color = color_gn_rd[color_index]
            led_set(0, 80, color)

            date = time.strftime("%Y-%m-%d",  time.strptime(str(ts), "%Y-%m-%d %H:%M:%S"))


# In[11]:

print 'Functions Available:'
print 'yearly_data()'
print 'daily_vs_past30days()'
print 'OneWeek_data()'


# In[ ]:



