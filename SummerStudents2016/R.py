from LEDsetup import*
led.update()
led.fill(Off)

def R (Color):
    r=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,53,54,57,61,62,63,64,65,66,67,71,72,74,75,76]
    for i in r:
        led.set(i,Color)
        led.update()
    return

R(White)
