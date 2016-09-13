from LEDsetup import*
led.fill(Off)
led.update()

def L(Color):
    l=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,62,71,72]
    for i in l:
        led.set(i,Color)
        led.update()
L(Red)

