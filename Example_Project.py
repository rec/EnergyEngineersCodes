
# coding: utf-8

# In[2]:

from DataFunctions import *


# ### Example Project
# ##### Top Row: Winter
# ##### Bottom Row: Summer
# ##### Monthly Average
# ##### Color scaled display

# In[ ]:

# Step 1: OPEN FILE
# Pick the data on bottom first, then data on top. 

[month1, year1, value1] = OpenMonthlyData('Dunne_Summer_Monthly_Average_KW.csv')
[month2, year2, value2] = OpenMonthlyData('Dunne_Winter_Monthly_Average_KW.csv')

#----------------------------------------#

# Step 2: GET MIN & MAX 

# We want both data to display on the same scale. 
# We choose the lowest of the lowest and highest of the highest value

min_value1 = min(value1)
max_value1 = max(value1)

min_value2 = min(value2)
max_value2 = max(value2)

min_value = min(min_value1,min_value2)
max_value = max(max_value1,max_value2)

#----------------------------------------#

# Step 3: SCALE DATA

color_low = Green
color_high = Red

clr_summer = ColorScaler(color_low, color_high, value1, min_value, max_value)
clr_winter = ColorScaler(color_low, color_high, value2, min_value, max_value)

#----------------------------------------#

# Step 4: Display data on LEDs
print ('Press control + C to stop the program')

while (True): ## TO CONTINUOUSLY REPEAT DATA

    Flash(5, 0.5, Purple) ## Flash everytime it starts over
    size = len(numLED_summer)

    for i in range(size):
        # Summer on Bottom --> LEDS 0-39. 

        led.fill(clr_summer[i], 0, 39)
        
        # Winter on TOP --> LEDS 40-79
        led.fill(clr_winter[i], 40, 79)
        
        led.update()
        time.delay(0.5)



