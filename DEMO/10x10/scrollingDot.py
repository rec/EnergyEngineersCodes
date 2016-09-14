from LEDsetup import*
led.fill(Off)
led.update()
x = int(raw_input('Enter an LED number 0 through 99: '))
        
def Dot(Color):
    for a in range(x,100,10):
        led.set(a,Color)
        led.update()
        time.sleep(0.3)
        led.fill(Off)
        led.update()
        
Dot(Blue)

