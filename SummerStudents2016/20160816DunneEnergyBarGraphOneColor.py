#This program kind of cheats when it comes to LED color selection. We forced
#the colors to be what we wanted.

from LEDsetup import*   
from DataFunctions import *
steps = 5
clrs = ColorScale(steps)

led.fill(Off)
led.update()
time.sleep(1)


#[timestamp, value] = OpenDailyData('daily_for_1year.csv')
[timestamp, value] = OpenDailyData('Dunne_Daily_Max_2015_KWH.csv')
large=max(value)
small=min(value)
gap=(large-small)/steps
for val in value:

    ## Group 1
    if ( (val >= small) & (val < small+gap) ):
        print val, 'is group 1'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x, Green)
        led.update()
        time.sleep(0.4)
        
        
    ## Group 2
    elif ( (val >= small+gap) & (val < small+2*gap) ):
        print val, 'is group 2'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x, Green)
        for y in range(2,100,10):
            led.set(y,Green)
        for z in range(3,100,10):
            led.set(z, Green)
        led.update()
        time.sleep(0.4)
        

    ## Group 3
    elif ( (val >= small+2*gap) & (val < small+3*gap) ):
        print val, 'is group 3'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x, Green)
        for y in range(2,100,10):
            led.set(y,Green)
        for z in range(3,100,10):
            led.set(z, Green)
        for a in range(4,100,10):
            led.set(a,Green)
        for b in range(5,100,10):
            led.set(b, Green)
        led.update()
        time.sleep(0.4)
       

    ## Group 4
    elif ( (val >= small+3*gap) & (val < small+4*gap) ):
        print val, 'is group 4'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x, Green)
        for y in range(2,100,10):
            led.set(y,Green)
        for z in range(3,100,10):
            led.set(z, Green)
        for a in range(4,100,10):
            led.set(a,Green)
        for b in range(5,100,10):
            led.set(b, Green)
        for c in range(6,100,10):
            led.set(c,Green)
        for d in range(7,100,10):
            led.set(d, Green)
        led.update()
        time.sleep(0.4)

    ## Group 5
    elif ( (val >= small+4*gap) & (val <= large) ):
        print val, 'is group 5'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x, Green)
        for y in range(2,100,10):
            led.set(y,Green)
        for z in range(3,100,10):
            led.set(z, Green)
        for a in range(4,100,10):
            led.set(a,Green)
        for b in range(5,100,10):
            led.set(b, Green)
        for c in range(6,100,10):
            led.set(c,Green)
        for d in range(7,100,10):
            led.set(d, Green)
        for e in range(8,100,10):
            led.set(e,Green)
        for f in range(9,100,10):
            led.set(f,Green)
        led.update()
        time.sleep(0.4)

    
