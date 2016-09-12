from LEDsetup import*
x= True
led.fill(Off)
led.update()
num = int(raw_input('Give me a Number: '))

if (num % 2 == 1):
    led.fill(Blue)
    led.update()
    time.sleep(1)
    led.fill(Off)
    led.update()
    print 'you have chosen a Odd Number!!'
    exit()
else:
    led.fill(Green)
    led.update()
    time.sleep(0.5)
    led.fill(Off)
    led.update()
    print 'you have chosen a Even joint!'
    exit()



