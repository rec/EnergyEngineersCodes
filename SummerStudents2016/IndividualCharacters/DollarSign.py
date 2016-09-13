from LEDsetup import*
led.fill(Off)
led.update()

def DollarSign(Color):
    ds=[41,42,43,44,45,46,47,16,26,36,56,66,76,15,14,24,34,54,64,74,63,73,12,22,32,52,62,72]
    for i in ds:
        led.set(i,Color)
        led.update()
    return

DollarSign(Lime)
