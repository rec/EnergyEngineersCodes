
# coding: utf-8

# In[57]:

import numpy as np
import csv
import time
#import matplotlib
#import matplotlib.pyplot as plt
#import pandas as pd
from LEDsetup import *


# ### Generating color scale

# In[55]:

def ColorScale(steps):
    clrs = []
    green = 180 #Green 255 is too bright
    red = 0
    inc = np.floor((255+180)/steps)
    
    ## INCREASING RED
    while(red < 255): ## start with green and increase red
        clrs.append((red, green, 0))
        red += inc;
    
    red = 255
    ## DECREASING GREEN
    while(green > inc): ## start with red + green and decrease green
        green -= inc;
        if(green < 6):
            green = 0; 
        clrs.append((red, green, 0)); 
        
    return clrs


# In[35]:

def OpenData(filename):
    time_stamp = []
    value = []
    with open(filename) as f:
        cf = csv.DictReader(f, fieldnames=['time_stamp', 'value'])
        for row in cf:
            time_stamp.append((row['time_stamp']))
            value.append(float(row['value']))
    
    return(time_stamp, value)


# In[49]:

def ScalingData(value, steps):
    scaling_index = []
    max_value = max(value)
    min_value = min(value)
    scale = (max_value - min_value+0.1)/steps 
    ## Without the +0.1, there is exactly 1 value that gets the index == steps. 
    ## We want indices from 0 to steps-1
    
    for i in value:
        scaling_index.append(np.floor(i/scale))
    return scaling_index
    


# In[53]:

#def PlotData(time_stamp, value):
    #plt.plot(time_stamp, value)
    #plt.xlabel('Time')
    #plt.ylabel('Energy Use in kWh')
    #plt.show()


# In[61]:

def DispColors(clrs):
    for i, color in enumerate(clrs):
        print('color '+ str(i+1))
        led.fill(color)
        led.update()
        time.sleep(0.4)


# In[ ]:



