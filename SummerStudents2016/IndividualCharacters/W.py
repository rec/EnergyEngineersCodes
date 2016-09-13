from LEDsetup import*
led.fill(Off)
led.update()

def W (Color):
    w=[12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,41,42,43,44,51,52,61,62,63,64,65,67,72,73,74,75,76,77]
    for i in w:
        led.set (i,Color)
        led.update()
    return

W(Blue)
