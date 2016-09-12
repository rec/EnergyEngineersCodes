from LEDsetup. import*
while(True):
    led.fill(White)
    led.update()
    led.fill(Red, 1,10)
    time.sleep(0.06)
    led.update()
    led.set(Blue,11)
    led.update()
    led.fill(Off)
    
    
