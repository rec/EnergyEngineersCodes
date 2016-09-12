from LEDsetup import*

led.fill(Off)
led.update()

for x in range(0,80,10):
    for i in range(0,9):
        led.set(x+10,Pink)
        led.set(i+4,Lime)
        led.update()
        time.sleep(0.5)
            
