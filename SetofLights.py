from LEDsetup import*
led.fill(Off)
led.update()

a=raw_input('How many lights do you want to turn? ')

n=int(a)

n=n-1


b=raw_input('How many seconds do you want the lights to stay on? ')

c=float(b)




led.fill(Pink,0,n)
led.update()
time.sleep(c)
led.fill(Off)
led.update()

led.update()
led.fill(Off)

    


  
  
  





