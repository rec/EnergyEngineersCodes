from LEDsetup import*
led.fill(Off)
led.update()

for i in range(255,0,-1):
    led.fill((i,0,0))
    led.update()
    



for i in range(0,254,1):
    led.fill((i,255,255))
    led.update()
 

for i in range(0,253,1):
    led.fill((i,255,75))
    led.update()


for i in range(0,252,1):
    led.fill((i,244,188))
    led.update()


led.fill(Off)
led.update()

