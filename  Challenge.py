from LEDsetup import*
led.fill(Off)
count= 0
while(count < 10):
    count = count + 1
    led.fill(Red)
    led.update()
    time.sleep(0.5)
    led.fill(Blue)
    led.update()
    time.sleep(0.5)
