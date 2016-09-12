from LEDsetup import*
led.fill(Brown)

led.update()

def Face(Color):
    face=[29,39,49,59,69,18,28,38,48,58,68,78,17,77,16,76,15,75,14,74,13,73,22,32,42,52,62,45,24,34,44,54,64]
    for i in face:
        led.set(i,Color)
        led.update()
    return


def Sunglasses(Color):
    sg=[27,37,47,57,67,26,36,46,56,66,25,35,55,65]
    for i in sg:
        led.set(i,Color)
        led.update()
    return


def Smile(Color):
    smile=[23,33,43,53,63]
    for i in smile:
        led.set(i,Color)
        led.update()
    return








Face(Yellow)

Sunglasses(Blue)

Smile(Pink)



