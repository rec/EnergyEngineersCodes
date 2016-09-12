from DataFunctions import *
steps = 5
clrs = ColorScale(steps)

[timestamp, value] = OpenData('daily_for_1year.csv')

for val in value:

    ## Group 1
    if ( (val >= small) & (val < small+gap) ):
        print val, 'is group 1'
        led.fill(clrs[0])
        time.sleep(0.4)
        
    ## Group 2
    if ( (val >= small+gap) & (val < small+2*gap) ):
        print val, 'is group 2'
        led.fill(clrs[1])
        time.sleep(0.4)

    ## Group 3
    if ( (val >= small+2*gap) & (val < small+3*gap) ):
        print val, 'is group 3'
        led.fill(clrs[2])
        time.sleep(0.4)

    ## Group 4
    if ( (val >= small+3*gap) & (val < small+4*gap) ):
        print val, 'is group 4'
        led.fill(clrs[3])
        time.sleep(0.4)

    ## Group 5
    if ( (val >= small+4*gap) & (val <= large) ):
        print val, 'is group 5'
        led.fill(clrs[4])
        time.sleep(0.4)
