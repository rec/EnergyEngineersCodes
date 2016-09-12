from LEDsetup import*
led.fill(Off)
led.update()

def K(Color):
    k=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,34,44,45,54,55,61,62,63,64,66,67,71,72,73,74,76,77]
    for i in k:
        led.set(i,Color)
        led.update()
    return
K(White)
