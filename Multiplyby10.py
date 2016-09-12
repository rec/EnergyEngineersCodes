from LEDsetup import*

i=raw_input('Give me a number and i will multiply it by five:')

Amaya= int(i)





print Amaya*5

for i in range (0,80,2):
        led.set(i,Purple)
        led.set(i+1,Turquoise)
        led.update()
        time.sleep(0.02)
for i in range (0,80,3):
        led.set(i,White)
        led.set(i+1,Lime)
        led.update()
        time.sleep(0.0025)
        
for i in range (0,80,4):
        led.set(i,Orange)
        led.set(i+1,Blue)
        led.update()
        time.sleep(0.05)
for i in range (0,80,5):
        led.set(i,Yellow)
        led.set(i+1,Pink)
        led.update()
        time.sleep(0.0025)
    
