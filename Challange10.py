from LEDsetup import*

led.fill(Off)
led.update()

for loopcount in range (0,80,10):
    led.fill (White,loopcount,loopcount+9)
    led.set(loopcount+2,Pink)
    led.set(loopcount+4,Blue)
    led.set(loopcount+6,Purple)
    led.set(loopcount+8,Lime)
    led.update()
    time.sleep(1)
    

   
    
