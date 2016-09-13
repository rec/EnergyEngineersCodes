from LEDsetup import *
led.fill(Off)
led.update()

count = 0

while True:
    while (count < 10):
        led.set(count, Pink)
        led.update()
        time.sleep(0.1)
        count = count + 1
    led.fill(Off)
    led.update()
    count = 0
    time.sleep(0.1)








   
    
    
	
	
