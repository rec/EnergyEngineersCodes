
# coding: utf-8

# In[ ]:

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
# Winter on Bottom --> LEDS 0-39. Summer on TOP --> LEDS 40-79

color_low = Green
color_high = Red
clr_summer = ColorScaler(0, 39, value1, min_value, max_value)
clr_winter = ColorScaler(40, 79, value2, min_value, max_value)

#----------------------------------------#

# Step 4: Display data on LEDs
print ('Press control + C to stop the program')

while (True): ## TO CONTINUOUSLY REPEAT DATA

    Flash(5, 0.5, Purple) ## Flash everytime it starts over

    summer_color = Yellow
    winter_color = Pink
    
    size = len(numLED_summer)

    for i in range(size):
        led.fill(summer_color, 0, numLED_winter[i])
        led.fill(winter_color, 40, numLED_summer[i])
        led.update()
        time.delay(0.5)



