from LEDsetup import*
led.fill(Off)
led.update()

def Q(Color):
    q=[12,13,14,15,16,21,22,23,24,25,26,27,31,37,41,43,47,51,52,57,60,61,62,63,64,65,66,67,70,71,73,74,75,76]
    for i in q:
            led.set(i,Color)
            led.update()
    return
Q(Brown)

