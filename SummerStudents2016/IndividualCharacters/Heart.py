from LEDsetup import*

led.fill(Off)
led.update()

def Heart(Color):
    heart=[41,32,23,14,15,16,17,27,36,45,56,67,77,76,75,74,63,52]
    for i in heart:
        led.set(i,Color)
    led.update()
    return
Heart(Red)
