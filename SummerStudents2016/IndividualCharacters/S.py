from LEDsetup import*
led.fill(Off)
led.update()

def S(Color):
        s=[17,27,37,47,57,67,77,16,26,66,76,15,25,14,24,34,44,54,64,63,73,62,72,12,22,11,21,31,41,51,61,71]
        for i in s:
             led.set(i,Color)
             led.update()
        return
S(Orange)
