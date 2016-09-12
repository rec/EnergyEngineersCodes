from LEDsetup import*
led.fill(Off)
led.update()

def Plus (Color):
    plus=[41,42,43,44,45,46,47,14,24,34,54,64,74]
    for i in plus:
        led.set(i,Color)
        led.update()
    return

Plus(Gold)
