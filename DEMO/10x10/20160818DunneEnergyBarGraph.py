#This program kindof cheats when it comes to LED color selection. We forced
#the colors to be what we watned.

from LEDsetup import*   
from DataFunctions import *
steps = 10
clrs = ColorScale(steps)

led.fill(Off)
led.update()
time.sleep(1)

#This is how long each data point flashing
flashtime = 0.1



#[timestamp, value] = OpenDailyData('daily_for_1year.csv')
[timestamp, value] = OpenDailyData('Dunne_Daily_Max_2015_KWH.csv')
large=max(value)
small=min(value)
gap=(large-small)/steps
for val in value:

    ## Group 1
    if ( (val >= small) & (val < small+gap) ):
        print val, 'is in group 1'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        led.update()
        time.sleep(flashtime)
        
        
    ## Group 2
    elif ( (val >= small+gap) & (val < small+2*gap) ):
        print val, 'is group 2'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))
        led.update()
        time.sleep(flashtime)
        

    ## Group 3
    elif ( (val >= small+2*gap) & (val < small+3*gap) ):
        print val, 'is group 3'
        led.fill(Off)             
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))   
        for y in range(2,100,10):
            led.set(y,(155,185,0))
        led.update()
        time.sleep(flashtime)
       

    ## Group 4
    elif ( (val >= small+3*gap) & (val < small+4*gap) ):
        print val, 'is group 4'
        led.fill(Off)            
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))
            
        for y in range(2,100,10):
            led.set(y,(155,185,0))
            
        for z in range(3,100,10):
            led.set(z,(180,175,0))
        led.update()
        time.sleep(flashtime)

    ## Group 5
    elif ( (val >= small+4*gap) & (val < small+5*gap) ):
        print val, 'is group 5'
        led.fill(Off)            
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))
            
        for y in range(2,100,10):
            led.set(y,(155,185,0))
            
        for z in range(3,100,10):
            led.set(z,(180,175,0))
            
        for a in range(4,100,10):
            led.set(a,(201,155,0))
    
        led.update()
        time.sleep(flashtime)




    ## Group 6
    elif ( (val >= small+5*gap) & (val < small+6*gap) ):
        print val, 'is group 6'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))
            
        for y in range(2,100,10):
            led.set(y,(155,185,0))
            
        for z in range(3,100,10):
            led.set(z,(180,175,0))
            
        for a in range(4,100,10):
            led.set(a,(201,155,0))
            
        for b in range(5,100,10):
            led.set(b,Yellow)
        led.update()
        time.sleep(flashtime)



    ## Group 7
    elif ( (val >= small+6*gap) & (val < small+7*gap) ):
        print val, 'is group 7'
        led.fill(Off)
        led.update()
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))

        for y in range(2,100,10):
            led.set(y,(155,185,0))

        for z in range(3,100,10):
            led.set(z,(180,175,0))

        for a in range(4,100,10):
            led.set(a,(201,155,0))
    
        for b in range(5,100,10):
            led.set(b,Yellow)

        for c in range(6,100,10):
            led.set(c,Orange)
        time.sleep(flashtime)


     ## Group 8
    elif ( (val >= small+7*gap) & (val < small+8*gap) ):
        print val, 'is group 8'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))

        for y in range(2,100,10):
            led.set(y,(155,185,0))

        for z in range(3,100,10):
            led.set(z,(180,175,0))

        for a in range(4,100,10):
            led.set(a,(201,155,0))

        for b in range(5,100,10):
            led.set(b,Yellow)

        for c in range(6,100,10):
            led.set(c,Orange)

        for d in range(7,100,10):
            led.set(d,(255,65,0))
        led.update()
        time.sleep(flashtime)



    
     ## Group 9
    elif ( (val >= small+8*gap) & (val < small+9*gap) ):
        print val, 'is group 9'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))

        for y in range(2,100,10):
            led.set(y,(155,185,0))

        for z in range(3,100,10):
            led.set(z,(180,175,0))

        for a in range(4,100,10):
            led.set(a,(201,155,0))

        for b in range(5,100,10):
            led.set(b,Yellow)

        for c in range(6,100,10):
            led.set(c,Orange)

        for d in range(7,100,10):
            led.set(d,(255,65,0))

        for e in range(8,100,10):
            led.set(e,(255,50,0))

        led.update()
        time.sleep(flashtime)



     ## Group 10
    elif ( (val >= small+9*gap) & (val <= large ) ):
        print val, 'is group 10'
        led.fill(Off)
        for i in range(0,100,10):
            led.set(i,Green)
        for x in range(1,100,10):
            led.set(x,(135,215,0))
            
        for y in range(2,100,10):
            led.set(y,(155,185,0))
            
        for z in range(3,100,10):
            led.set(z,(180,175,0))
            
        for a in range(4,100,10):
            led.set(a,(201,155,0))
            
        for b in range(5,100,10):
            led.set(b,Yellow)
            
        for c in range(6,100,10):
            led.set(c,Orange)
            
        for d in range(7,100,10):
            led.set(d,(255,65,0))
            
        for e in range(8,100,10):
            led.set(e,(255,50,0))
            
        for f in range(9,100,10):
            led.set(f,Red)
        led.update()
        time.sleep(flashtime)

led.fill(Off)
led.update()

        
