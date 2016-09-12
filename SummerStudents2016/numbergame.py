from LEDsetup import*
from random import randrange
red = raw_input('Give me a number, i will multiply it by 8(0-31):')
random_number = randrange(8)
red = random_number
print red*random_number*3
blue = raw_input('Give me another number, i will multiply it by 8(0-31):')
blue = int(blue)
random_number = randrange(8)
blue = random_number
print blue*random_number*3
green = raw_input('What was your answer?(0-31)')
green = int(green)
random_number = randrange(8)
green = random_number*3
print green*random_number



led.fill((red,blue,green))
led.update()
time.sleep(0.5)
led.update()
led.fill((red,blue,green))
led.update()
time.sleep(0.5)
led.update()
led.fill((red,blue,green))
led.update()






