from LEDsetup import*

led.fill(Off)
led.update()

def G(color):
   g = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,43,47,51,52,53,57,62,63,66,67,71,72,73,76,77]
   for i in g:
        led.set(i,color)
        led.update()
   return

G(Red)
