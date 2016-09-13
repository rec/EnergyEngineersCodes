from LEDsetup import*

led.fill(Off)
led.update()

color = raw_input('what color would you like? blue = y, red = x, green = z: ')

if color == 'x':
    for a in range(0,80,1):
        led.set(a,(a+29,0,0))
        led.update()
           

elif color == 'y':
    for a in range(0,80,1):
        led.set(a,(0,0,a+29))
        led.update()


elif color == 'z':
    for a in range(0,80,1):
        led.set(a,(0,a+29,0))
        led.update()

           
    

