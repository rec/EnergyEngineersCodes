from LEDsetup import *

num = int(raw_input('Enter a value: '))

if(num % 2 == 0 ):
    led.fill(Green)
    led.update()
    print "that's even brah!"
else:
    led.fill(Blue)
    led.update()
    print "tht's odd brah"

