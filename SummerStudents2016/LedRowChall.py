from LEDsetup import*

led.fill(Off)
led.update()


num = int(raw_input('How many lights do you want to turn on: '))
Num = int(raw_input(' One more number please, : '))
Color = num,Num
while(True):
    led.fill(Off)
    led.update()
    Color = led.fill(Gold,num,Num)
    led.update()
    time.sleep(1)
    led.update()
    led.fill(Off)
    led.update()
    Color = led.fill(Blue,num,Num)
    led.update()
    time.sleep(1)
    led.update()
       



