from LEDsetup import*
led.fill(Off)
led.update()

def N(color):
    n = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,36,45,54,63,71,72,73,74,75,76,77]
    for i in n:
        led.set(i,color)
        led.update()
N(Yellow)
