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

def Plus (Color):
    plus=[41,42,43,44,45,46,47,14,24,34,54,64,74]
    for i in plus:
        led.set(i,Color)
        led.update()
    return

Plus(Gold)

def Minus(Color):
    minus=[14,24,34,44,54,64,74]
    for i in minus:
        led.set(i,Color)
        led.update()
    return

Minus(Gold)

def Period(Color):
    period=[53,63,73,52,62,72,51,61,71]
    for i in period:
        led.set(i,Color)
        led.update()
    return

Period(Lime)



def Pound(Color):
    pound=[31,32,33,34,35,36,37,61,62,63,64,65,66,67,15,25,45,55,75,13,23,43,53,73]
    for i in pound:
        led.set(i,Color)
        led.update()
    return

Pound(Blue)


def Percent (Color):
    percent=[17,27,37,16,15,36,35,25,11,22,33,44,55,66,77,53,63,73,72,52,51,61,71]
    for i in percent:
        led.set(i,Color)
        led.update()
    return
Percent(Gray)

def DollarSign(Color):
    ds=[41,42,43,44,45,46,47,16,26,36,56,66,76,15,14,24,34,54,64,74,63,73,12,22,32,52,62,72]
    for i in ds:
        led.set(i,Color)
        led.update()
    return

DollarSign(Lime)

def Zero(Color):
    zero=[11,12,13,14,15,16,17,21,27,31,34,37,41,47,51,57,61,62,63,64,65,66,67,71,72,73,74,75,76,77,76]
    for i in zero:
        led.set(i,Color)
        led.update()
    return

Zero(White)







