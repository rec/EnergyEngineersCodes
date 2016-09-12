from LEDsetup import*

A= raw_input('I will square any given numer, give me a number:')
# A is a string

B=int(A)
#B is the same as A, but it's an integer

C = B**2

print C

C=True
if C:
    led.fill((255,140,0))
    led.update()
    led.fill(Off)
    

red= raw_input('Pick a number')
blue= raw_input('Pick a number')
green= raw_input('Pick a number')
red = int(red)
blue = int(blue)
green = int(green)
led.fill(Off)
led.update()
led.fill((red,blue,green))
led.update()
