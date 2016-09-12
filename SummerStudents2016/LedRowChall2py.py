from LEDsetup import*

led.fill(Off)
led.update()


num = int(raw_input('What start position would you like the lights to be in? '))
Num = int(raw_input(' What end position would you like the lightsa to be in? '))
Seconds = float(raw_input('how long would you like the lights to be on? '))
m = int(raw_input('how many times would you like it to blink? '))
Color = raw_input('What color would you like to use?')



for blink in range(m): 
    led.fill Color,(num,Num)
    led.update()
    time.sleep(float(Seconds))
    led.fill(Off)
    led.update()
    led.fill Color,(num,Num)
    led.update()
    time.sleep(float(Seconds))
    led.update()
    led.fill(Off)
    led.update()



