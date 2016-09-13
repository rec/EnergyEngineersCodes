from LEDsetup import*
led.fill(Off)
led.update()

def Pound(Color):
    pound=[31,32,33,34,35,36,37,61,62,63,64,65,66,67,15,25,45,55,75,13,23,43,53,73]
    for i in pound:
        led.set(i,Color)
        led.update()
    return

Pound(Blue)
