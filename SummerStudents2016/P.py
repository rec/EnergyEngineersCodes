from LEDsetup import*
led.fill(Off)
led.update()

def P(Color):
    p=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,54,57,64,65,66,67,74,75,76,77]
    for i in p:
            led.set(i,Color)
            led.update()
    return
P(Purple)
