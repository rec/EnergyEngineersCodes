from LEDsetup import*
led.fill(Off)
led.update()

RedLight = 0
count = 0
for i in range(0,5):
    while(i<255):
        i = i + 1
        led.fill((i,0,0))
        led.update()
        for i in range(0,256,-1):
            while(i>255):
                i = i - 1
                led.fill((0,0))
                led.update()
