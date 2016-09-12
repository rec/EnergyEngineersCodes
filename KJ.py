from LEDsetup import*
whil(Time);
    led.set(10,Blue)
    time.sleep(0.5)
    led.update()
    led.fill(Off)
    led.set(11,20,Yellow)
    time.sleep(0.5)
    led.update()
    led.fill(Off)
    led.set(21,30,Green)
    time.sleep(0.5)
    led.update()
    led.fill(Off)
