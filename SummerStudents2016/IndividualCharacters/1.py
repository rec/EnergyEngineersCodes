from LEDsetup import*
led.fill(Off)
led.update()

def One(Color):
    one=[11,16,17,21,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,61]
    for i in one:
        led.set(i,Color)
        led.update()
    return
One(Blue)
