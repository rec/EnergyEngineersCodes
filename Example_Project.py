
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

# Step 3a: SCALE DATA BY COLOR. TO SCALE DATA BY NUMBER, look at step 3b.

color_low = Green
color_high = Red

clr_summer = ColorScaler(color_low, color_high, value1, min_value, max_value)
clr_winter = ColorScaler(color_low, color_high, value2, min_value, max_value)

#----------------------------------------#

# Step 3b : SCALE DATA BY NUMBER OF LEDs
# Using entire 80 LEDs to scale the summer data alone. 
# If you are only using the bottom panel, do the command twice - once with summer and once with winter. 
# Numscaler() returns the last LED to be turned on. 
# So for the bottom panel, turn on from 0 --> NumLEDs. For the top panel turn on 40 --> numLEDs.

numLED_all = NumScaler(0, 79, value1, min_value, max_value)
# Bottom panel is LEDs 0,39 for the first two numbers. Top panel is LEDs 40, 79. All LEDs are 0, 79. 

#----------------------------------------#

# Step 4a: Display COLOR data on LEDs
# This displays data once and stops
print ('Displaying COLOR data')

Flash(5, 0.5, Purple) ## Flash everytime it starts over
size = len(clr_summer)

for i in range(size):
    # Summer on Bottom --> LEDS 0-39. 

    led.fill(clr_summer[i], 0, 39)

    # Winter on TOP --> LEDS 40-79
    led.fill(clr_winter[i], 40, 79)

    led.update()
    time.delay(0.5)


#----------------------------------------#

# Step 4b: Display NUMBER data on LEDs
# This displays data continuously

print ('Displaying NUMBER DATA')

color_summer = Yellow

# We are letting the user know how to stop this program
print ('Press control + C to stop the program')

while (True): ## TO CONTINUOUSLY REPEAT DATA
    
    Flash(5, 0.5, Purple) ## Flash everytime it starts over
    size = len(numLED_all)

    for i in range(size):
        # Summer on all panels --> LEDS 0-79. 

        led.fill(color_summer, 0, numLED_all[i])
        led.update()
        time.delay(0.5)


