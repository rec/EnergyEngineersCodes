
from LEDsetup import*
led.fill(Off)
led.update()

def Minus(Color):
    minus=[14,24,34,44,54,64,74]
    for i in minus:
        led.set(i,Color)
        led.update()
    return

Minus(Gold)





