#This program kindof cheats when it comes to LED color selection. We forced
#the colors to be what we watned.

from LEDsetup import*   
from DataFunctions import *
steps = 5
clrs = ColorScale(steps)


#[timestamp, value] = OpenDailyData('daily_for_1year.csv')
[timestamp, value] = OpenDailyData('Dunne_Daily_Max_2015_KWH.csv')
large=max(value)
small=min(value)
gap=(large-small)/steps
for val in value:

    ## Group 1
    if ( (val >= small) & (val < small+gap) ):
        print val, 'is group 1'
        led.fill(Green)
        led.update()
        time.sleep(0.4)
        
    ## Group 2
    if ( (val >= small+gap) & (val < small+2*gap) ):
        print val, 'is group 2'
        led.fill(Purple)
        led.update()
        time.sleep(0.4)

    ## Group 3
    if ( (val >= small+2*gap) & (val < small+3*gap) ):
        print val, 'is group 3'
        led.fill(Yellow)
        led.update()
        time.sleep(0.4)

    ## Group 4
    if ( (val >= small+3*gap) & (val < small+4*gap) ):
        print val, 'is group 4'
        led.fill(Turquoise)
        led.update()
        time.sleep(0.4)

    ## Group 5
    if ( (val >= small+4*gap) & (val <= large) ):
        print val, 'is group 5'
        led.fill(Red)
        led.update()
        time.sleep(0.4)
