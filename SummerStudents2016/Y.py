from LEDsetup import*
led.fill(Off)
led.update()

def Y(Color):
    y=[15,16,17,21,24,25,26,27,31,34,41,44,51,54,61,62,63,64,65,66,67,71,72,73,74,75,76,77]
    for i in y:
        led.set(i,Color)
        led.update()
    return
Y(Blue)
    
