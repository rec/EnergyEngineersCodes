from LEDsetup import*
led.fill(Off)
led.update()

def U(Color):
    u=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,71,72,73,74,75,76,77]
    for i in u:
        led.set(i,Color)
        led.update()
    return

U(Turquoise)
