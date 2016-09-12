from LEDsetuup import*
while(True):
    led.fill(Green,1,20)
    time.sleep(0.8)
    led.update()
    led.fill(Off)
    led.set(Blue,21,30)
    time.sleep(0.8)
    led.update()
    led.set(Yellow,31,40)
    ti.sleep(0.8)
    led.update()
