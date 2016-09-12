

from LEDsetup import*
led.fill(Off)
led.update()
i= raw_input('Type a  Odd Number: ')
num=int(i)


if (num % 2 == 1 ):
     led.fill(Purple)
     led.update()
    
else:
    led.fill(Red)
    led.update()
















