from LEDsetup import*

led.fill(Off)
led.update()

def E(color):
    e=[17,27,37,47,57,67,77,16,66,76,15,14,24,34,44,54,13,23,31,34,41,44,51,54,61,62,71,72,11,12,13,21,22,23,24]
    for i in e:
        led.set(i,color)
        led.update()
    return

E(Lime)
