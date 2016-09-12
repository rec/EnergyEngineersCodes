from LEDsetup import*

led.fill(Off)
led.update()
for lights in range(0,80,10):
    led.set(lights+1,Blue)
    led.set(lights+3,White)
    led.set(lights+5,Yellow)
    led.set(lights+7,Pink)
    led.set(lights+9,Red)
    led.set(lights+11,Lime)
    led.update()
    time.sleep(1)
    
