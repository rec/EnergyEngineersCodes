
# coding: utf-8

# In[ ]:

from DataFunctions import *


# ### Group 1:
# ###### Wants the top of the lamp to show data from the summer; bottom to show data from the winter.  Display monthly average for each where the number of leds that light up indicated the amount of energy used.  since its monthly average the data will be updated 3x then repeat.

# In[ ]:


def Group1():
    # Step 1: OPEN FILE
    # Pick the data on bottom first, then data on top. 

    [month1, year1, value1] = OpenMonthlyData('Dunne_Winter_Monthly_Average_KW.csv')
    [month2, year2, value2] = OpenMonthlyData('Dunne_Summer_Monthly_Average_KW.csv')

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

    numLED_winter = NumScaler(0, 39, value1, min_value, max_value)
    numLED_summer = NumScaler(40, 79, value2, min_value, max_value)

    #----------------------------------------#

    # Step 4b: Display data on LEDs
    while (True): ## TO CONTINUOUSLY REPEAT DATA
        print ('Press control + C to stop the program')

        Flash(5, 0.5, Purple) ## Flash everytime it starts over

        summer_color = Yellow
        winter_color = Pink

        for i in range(3):
            led.fill(winter_color, 0, numLED_winter[i])
            led.fill(summer_color, 40, numLED_summer[i])
            led.update()
            time.delay(0.5)
        
        
    


# ### Group 2:
# ###### Top of lamp is Lindblom, bottom is Dunne; using color scale show the daily maximum.  flash at the beginning of a new week.

# In[ ]:

def Group2():
    # Step 1: OPEN FILE
    # Pick the data on bottom first, then data on top. 

    [time_stamp1, value1] = OpenDailyData('Dunne_Daily_Max_2015_KWH.csv')
    [time_stamp2, value2] = OpenDailyData('Lindblom_Daily_Max_2015_KWH.csv')

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
    # Dunne on Bottom --> 0 to 39. Lindblom on TOP --> LEDS 40-79
    
    color_low = Green
    color_high = Red

    clr_dunne = ColorScaler(color_low, color_high, value1, min_value, max_value)
    clr_lindblom = ColorScaler(color_low, color_high, value2, min_value, max_value)
    #----------------------------------------#

    # Step 4: Display data on LEDs

    count = 1

    Flash(5, 0.5, Purple)
    ###number of times, ###delay, ###color) ## Flash at the beginning

    for i in range(364):
        led.fill(clr_dunne[i], 0, 39)
        led.fill(clr_lindblom[i], 40, 79)
        led.update()

        if (count == 7):
            Flash(5, 0.5, Purple) ## at number = 7, counting from 0. End of the week. 
            count = 1

        count = count + 1
        
        time.sleep(0.5)

            

        
        


# 
# ### Group 3: 
# ###### Like group 1 but with a color scale instead of a number scale, and daily data average instead of monthly

# In[ ]:

def Group3():
    # Step 1: OPEN FILE
    # Pick the data on bottom first, then data on top. 

    [month1, year1, value1] = OpenDailyData('Dunne_Winter_Daily_Average_KW.csv')
    [month2, year2, value2] = OpenDailyData('Dunne_Summer_Daily_Average_KW.csv')

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
    # Winter on Bottom --> 0 to 39. Summer on TOP --> LEDS 40-79
    
    color_low = Green
    color_high = Red

    clr_winter = ColorScaler(color_low, color_high, value1, min_value, max_value)
    clr_summer = ColorScaler(color_low, color_high, value2, min_value, max_value)
    #----------------------------------------#

    # Step 4: Display data on LEDs

    while (True): ## TO CONTINUOUSLY REPEAT DATA
        print ('Press control + C to stop the program')

        Flash(5, 0.5, Purple) ## Flash everytime it starts over

        for i in range(3):
            led.fill(clr_winter[i], 0, 39)
            led.fill(clr_summer[i], 40, 79)
            led.update()
            time.sleep(0.5)
        
        


# ### Group 4:
# ###### wants the top of the lamp to show data from Dunne; bottom to show data from Lindblom. Display monthly averages as colors. All top row lights will flash the same color depending on Dunne’s usage. All bottom row lights will flash the same color depending on Lindblom’s usage. Flash between months. Repeat

# In[ ]:

def Group4():
    # Pick the data on bottom first, then data on top. 
    
    [month1, year1, value1] = OpenMonthlyData('Lindblom_Monthly_Average_2015_KW.csv')
    [month2, year2, value2] = OpenMonthlyData('Dunne_Monthly_Average_2015_KW.csv')

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
    # Winter on Bottom --> 0 to 39. Summer on TOP --> LEDS 40-79
    
    color_low = Green
    color_high = Red

    clr_lindblom = ColorScaler(color_low, color_high, value1, min_value, max_value)
    clr_dunne = ColorScaler(color_low, color_high, value2, min_value, max_value)
    #----------------------------------------#

    # Step 4: Display data on LEDs
    
    size = len(clr_Lindblom)
    for i in range(size):
        led.fill(clr_lindblom[i], 0, 39)
        led.fill(clr_dunne[i], 40, 79)
        led.update()
        
        time.sleep(0.5)

        Flash(###number of times, ###delay, ###color) ## at number = 7, counting from 0. End of the week. 
        


# In[ ]:

print ('Displaying Group 1')
Group1()

print ('Displaying Group 2')
Group2()

print ('Displaying Group 3')
Group3()

print ('Displaying Group 4')
Group3()

