from LEDsetup import*
led.fill(Off)
led.update()

def Percent (Color):
    percent=[17,27,37,16,15,36,35,25,11,22,33,44,55,66,77,53,63,73,72,52,51,61,71]
    for i in percent:
        led.set(i,Color)
        led.update()
    return
Percent(Gray)
