from LEDsetup import*
led.fill(Off)
led.update()

a=raw_input('How many lights do you want to turn? ')

n=int(a)

n=n-1


b=raw_input('How many seconds do you want the lights to stay on? ')

c=float(b)



d=raw_input('How many times do you want the lights to blink? ')

m=int(d)


#pretend user enters 3, so we want lights to blink three times...

for i in range(m):
    led.fill(Pink,0,n)
    led.update()
    time.sleep(c)   
    led.fill(Off)
    led.update()
    time.sleep(c) 

