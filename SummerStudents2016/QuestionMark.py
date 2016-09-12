from LEDsetup import*
led.fill(Off)
led.update()

def Question(Color):
    question=[17,27,37,47,57,67,16,26,55,56,66,65,34,44,54,64,33,43,31,41]
    for i in question:
        led.set(i,Color)
        led.update()
    return

Question(Turquoise)
