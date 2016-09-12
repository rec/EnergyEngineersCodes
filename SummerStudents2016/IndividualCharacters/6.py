from LEDsetup import*
led.fill(Off)
led.update()


def Six(Color):
    six=[11,12,13,14,15,16,17,21,24,25,26,27,31,34,37,41,44,47,51,54,57,61,62,63,64,66,67,71,72,73,74,76,77]
    for i in six:
        led.set(i,Color)
        led.update()
    return
Six(White)
        
