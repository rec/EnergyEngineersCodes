from LEDsetup import*
led.fill(Off)
led.update()

def Five(Color):
    five=[11,12,15,16,17,21,25,26,27,31,35,37,41,45,47,51,55,57,61,62,63,64,65,67,71,72,73,74,75,77]
    for i in five:
        led.set(i,Color)
        led.update()
    return
Five(Lime)
