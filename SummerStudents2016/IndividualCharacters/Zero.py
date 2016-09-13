from LEDsetup import*
led.fill(Off)
led.update()

def Zero(Color):
    zero=[11,12,13,14,15,16,17,21,27,31,34,37,41,51,57,61,62,63,64,65,66,67,71,72,73,74,75,76,77,76]
    for i in zero:
        led.set(i,Color)
        led.updat()
    return

    Zero(White)

