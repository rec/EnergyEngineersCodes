from LEDsetup import*
x=True
nam=raw_input('who are you?')
if nam == 'Amaya':
    print ' Welcome Amaya '
else:
    print 'You Thought!! Now exit by clicking the x at the top'
    x=False
if x:
    led.fill((255,140,0))
    led.update()
    led.fill(Off)
else:
    led.fill(Green,0,80)
    led.update()
    time.sleep(0.30)
    led.fill(Off)
    led.update()
    time.sleep(0.07)
    led.fill(Red,21,40)
    time.sleep(0.5)
    led.fill(Off)
    led.update()
    time.sleep(0.7)
    led.fill(Red,41,60)
    led.update()
    time.sleep(0.07)
    led.fill(Off)
    led.update()
    led.fill(Red,0,80)
    led.update()
    time.sleep(0.20)
    led.fill(Off)
    
    exit()
red=raw_input('What is the month of your Birthday?')
blue=raw_input('Solve this Equation: 60+1x60+0=')
green=raw_input('Add the pair of arms,hands,legs,eyes,and feet you have. What do yo get?')
red = int(red)
blue = int(blue)
green = int(green)
led.fill(Off)
led.update()
led.fill((red,blue,green))
led.update()
