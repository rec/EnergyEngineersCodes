from LEDsetup import*

led.fill(Off)
led.update()

def F(color):
   f = [11,12,13,14,15,16,17,21,22,23,24,34,44,54,27,37,47,57,67,77,76] 
   for i in f:
        led.set(i,color)
        led.update()
   return

F(Lime)
