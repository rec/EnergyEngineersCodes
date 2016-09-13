from LEDsetup import*
led.fill(Off)
led.update()



m = int(raw_input('how many times would you like it to blink? '))



for blink in range(m):
    for i in range(0,256):
            led.fill((i,0,0))
            led.update()

    for i in range(0,256):
            led.fill((255,100,0))
            led.update()
        


    for i in range(255,-1,-1):
            led.fill((255,100,0))
            led.update()


            
    for i in range(255,-1,-1):
            led.fill((255,155,0))
            led.update()

