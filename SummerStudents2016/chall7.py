from LEDsetup import *
count = 0
while (count < 10):
    count = count = + 1
    led.fill(Red)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    led.update()
    led.fill(Green)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    led.update()
    
	
	
