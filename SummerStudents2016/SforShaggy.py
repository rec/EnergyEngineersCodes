from LEDsetup import*
led.fill(Off)
led.update()

#led.fill()
#led.update()

#led.fill(Green,43,45)
#led.set(57,Green)
#led.set(62,Green)
#led.set(76,Green)
#led.set(84,Green)
#led.set(94,Green)
#led.set(97,Green)
#led.set(103,Green)
#led.set(104,Green)
#led.update()


def S(Color):
    
    s=[43,44,45,57,62,76,84,94,97,103,104]
    for i in s:
        led.set(i,Color)
        led.update()
    return







S(Purple)
