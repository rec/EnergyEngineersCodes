from LEDsetup import*
while(True):
    led.fill(Pink)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    led.update()
    time.sleep(0.5)
    led.fill(Green)
    led.update()
    time.sleep(0.5)
    led.fill(White)
    led.update()
    time.sleep(0.5)
    led.set(1,10,Purple)
    led.update()
    time.sleep(0.5)
    
    
