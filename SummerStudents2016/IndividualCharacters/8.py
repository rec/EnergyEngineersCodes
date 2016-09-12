from LEDsetup import*
led.fill(Off)
led.update()

def Eight(Color):
    eight=[11,12,13,15,16,17,21,22,23,25,26,27,31,34,37,41,44,47,51,54,57,61,64,67,71,72,73,75,76,77,24]
    for i in eight:
        led.set(i,Color)
        led.update()
    return
Eight(Orange)
