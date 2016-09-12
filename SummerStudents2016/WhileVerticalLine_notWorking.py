from LEDsetup import*
led.fill(Off)
led.update()

Color = Blue


for a in range(0,100,10):
       while True:
       led.fill(Color,a+5,9+5)
       led.update()
       led.fill(Off)
       led.update()
