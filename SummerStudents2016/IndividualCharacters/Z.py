from LEDsetup import*
led.update()
led.fill(Off)

def Z (Color):
    z=[17,27,37,47,67,77,57,16,26,56,66,76,45,55,24,34,44,54,64,43,33,12,22,32,62,72,11,21,31,41,51,61,71]
    for i in z :
        led.set(i,Color)
        led.update()
    return

Z(Pink)
