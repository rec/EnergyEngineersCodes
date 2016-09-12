from LEDsetup import*

led.fill(Off)
led.update()

for loopcount in range(0,10,1):
    led.fill(Red)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    led.fill(Green)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    
