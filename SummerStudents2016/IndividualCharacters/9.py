from LEDsetup import*
led.fill(Off)
led.update()

def Nine(Color):
    nine=[14,15,16,17,24,25,26,27,34,37,44,47,54,57,61,62,63,64,67,71,72,73,74,75,76,77]
    for i in nine:
        led.set(i,Color)
        led.update()
    return
Nine(Brown)
