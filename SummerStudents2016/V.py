from LEDsetup import*
led.fill(Off)
led.update()

def V(Color):
        v=[17,27,67,77,16,26,66,76,15,25,55,65,14,24,54,64,13,23,43,53,12,22,42,52,11,21,31,41 ]
        for i in v:
             led.set(i,Color)
             led.update()
        return

V(Purple)
