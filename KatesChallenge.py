from LEDsetup import*
led.fill(Off)
led.update()

b=raw_input('Choose  a number to pick a color: ')
a=int(b)
a=a

light= 0
while(light < 5):
    light = light + 1
   
    led.fill((light,255,1))
 
    led.update()


           
        
          
led.fill(Off)
led.update()




    
                
