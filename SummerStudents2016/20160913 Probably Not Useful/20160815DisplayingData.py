from DataFunctions import*

led.fill(Off)

steps = 5

clrs = ColorScale(steps)

led.fill(clrs[0])
led.update()
time.sleep(1)
led.fill(Off)
time.sleep(1)

led.fill(clrs[1])
led.update()
time.sleep(1)
led.fill(Off)
time.sleep(1)

led.fill(clrs[2])
led.update()
time.sleep(0.5)
led.fill(Off)
time.sleep(0.5)

led.fill(clrs[3])
led.update()
time.sleep(0.5)
led.fill(Off)
time.sleep(0.5)

led.fill(clrs[4])
led.update()
time.sleep(0.5)
led.fill(Off)
time.sleep(0.5)

