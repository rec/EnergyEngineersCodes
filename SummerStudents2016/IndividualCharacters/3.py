from LEDsetup import*
led.fill(Off)
led.update()

def Three(Color):
        three=[17,27,37,47,57,16,26,56,55,34,44,54,74,63,73,62,72,12,11,21,31,41,51,61,71,64,22]
        for i in three:
            led.set(i,Color)
            led.update()
        return
Three(White)
