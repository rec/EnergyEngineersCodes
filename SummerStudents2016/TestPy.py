from LEDsetup import *
print 'How many LEDs do you want to turn on?'
num = int(raw_input('Enter a number between 0 and 24: '))
led.fill(Red, 0, num)
led.update()
