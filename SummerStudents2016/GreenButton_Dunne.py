
# coding: utf-8

# ### Import libraries

# In[1]:


import csv
import numpy as np
import time

from datetime import datetime

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
import bibliopixel.colors as colors


# ### Generating color scale

# In[21]:

red = 0
green = 100
stepSize = 50
color_gn_rd = []
color_gn_rd.append((red, green, 0)) ## the lights are GRB format


# In[22]:

while(red < 205): ## start with green and increase red
    red += stepSize;
    color_gn_rd.append((red, green, 0))

while(green > 0): ## start with red + green and decrease green
    green -= stepSize;
    if(green < 6):
        green = 0; 
    color_gn_rd.append((red, green, 0)); 
    
total_colors = len(color_gn_rd)
total_colors


# ### Setting up LEDs

# In[ ]:

LedsPerSide = 10
numLeds= LedsPerSide*4*2 ##x/side * 4 sides * 2 levels
driver=DriverLPD8806(numLeds, ChannelOrder.BRG)
led=LEDStrip(driver)


# ### Defining Flashing modes

# In[12]:

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


# ### Displaying Daily Total Values for the entire year of data

# In[17]:

def yearly_data():
    time_stamp = []
    value = []
    with open('df_DailyAverage_Dunne.csv') as f:
        cf = csv.DictReader(f, fieldnames=['time_stamp', 'value'])
        for row in cf:
            time_stamp.append(row['time_stamp'])
            value.append(float(row['value']))
            max_value = max(value)
            min_value = min(value)
            ScalingSteps = (max_value + 0.1 - min_value)/(total_colors)
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'
        
        for ts, val in zip(time_stamp,value):
            print 'Date: ', ts
            print 'Average use: ', val
            color_index = int((val - min_value)/ScalingSteps)
            #print color_index
            #print color_index
            color = color_gn_rd[color_index]
            led_set(0, 80, color)
            time.sleep(0.5)


# ### Displaying Daily Energy Usage on Bottom with last 30 days' average on Top

# In[6]:

def daily_vs_past30days():
    time_stamp = []
    value = []
    with open('df_DailyAverage_Dunne.csv') as f:
        cf = csv.DictReader(f, fieldnames=['time_stamp', 'value'])
        for row in cf:
            time_stamp.append(row['time_stamp'])
            value.append(float(row['value']))
            
    average = []
    with open('df_RollingMean.csv') as f:
        cf = csv.DictReader(f, fieldnames=['time_stamp', 'value'])
        for row in cf:
            try:
                average.append(float(row['value']))
            except:
                average.append(float('nan'))
    max_value = max(value)
    min_value = min(value)
    ScalingSteps = (max_value + 0.1 - min_value)/total_colors
            
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'

        for ts, val, av in zip(time_stamp, value, average):
            print 'Date: ', ts
            print 'Total use: ', val
            color_index = int((val-min_value)/ScalingSteps)

            # print color_index
            color = color_gn_rd[color_index]
            led_set(0, 40, color)

            print 'Last 30 days average: ', av
            try:
                color_index = int(av/ScalingSteps)
                color = color_gn_rd[color_index]
                led_set(40, 80, color)

            except:
                color = (0,0,0)
                led_set(40, 80, color)

            time.sleep(0.4)
    


# ### Displaying 1 Week's Energy Use (res: every half-hour )

# In[7]:

def OneWeek_data():
    time_stamp = []
    value = []
    with open('df_1Week_Dunne.csv') as f:
        cf = csv.DictReader(f, fieldnames=['time_stamp', 'value'])
        for row in cf:
            time_stamp.append(row['time_stamp'])
            value.append(float(row['value']))

    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    max_value = max(value)
    min_value = 10 # there is a zero value that looks wrong. 
                   # There is a better way to avoid zero values. I will remove them soon. 
    ScalingSteps = (max_value + 0.1 - 10)/total_colors
    date = []
    while (True):
        print 'Starting Display'
        print 'Press \'Control + C\' to stop'
        
        count = 0
        for ts, val in zip(time_stamp, value):
            
            
            if(date != time.strftime("%Y-%m-%d",  time.strptime(ts, "%Y-%m-%d %H:%M:%S"))):
                print days[count]
                led_pulse(0, 80, (0,0,255))
                count = count + 1

            print 'Time: ', ts
            print 'Electricity Usage: ', val
            color_index = int((val)/ScalingSteps)

            #print color_index
            try:
                color = color_gn_rd[color_index]
                led_set(0, 80, color)
                time.sleep(0.4)
            except: 
                color = color_gn_rd[0]
                led_set(0, 80, color)
                time.sleep(0.4)
                

            date = time.strftime("%Y-%m-%d",  time.strptime(ts, "%Y-%m-%d %H:%M:%S"))


# In[8]:

print 'Functions Available:'
print 'yearly_data()'
print 'daily_vs_past30days()'
print 'OneWeek_data()'

