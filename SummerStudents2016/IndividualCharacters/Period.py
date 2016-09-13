from LEDsetup import*
led.fill(Off)
led.update()

def Period(Color):
    period=[53,63,73,52,62,72,51,61,71]
    for i in period:
        led.set(i,Color)
        led.update()
    return

Period(Lime)
