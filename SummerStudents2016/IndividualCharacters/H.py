from LEDsetup import*

led.fill(Off)
led.update()

def H(color):
   h = [17,27,16,26,15,25,14,24,13,23,12,22,11,21,34,44,54,64,74,67,77,66,76,65,75,64,74,63,73,62,72,61,71]
   for i in h:
        led.set(i,color)
        led.update()
   return

H(Blue)
