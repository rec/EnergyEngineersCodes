from LEDsetup import*
led.fill(Off)
led.update()


def Seven(Color):
    seven=[16,17,27,37,47,51,52,53,54,57,61,62,63,64,65,66,67,75,76,77]
    for i in seven:
            led.set(i,Color)
            led.update()
    return

Seven(Purple)
