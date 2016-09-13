from LEDsetup import*

led.fill(Off)
led.update()

def I(color):
   i= [17,27,37,47,57,67,77,36,46,56,35,45,55,34,44,54,33,43,53,32,42,52,11,21,31,41,51,61,71]
   for i in i:
        led.set(i,color)
        led.update()
   return

I(Orange)
