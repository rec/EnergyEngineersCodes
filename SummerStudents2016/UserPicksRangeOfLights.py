from LEDsetup import*



num = int(raw_input('How many lights do you want to turn on: '))
Num = int(raw_input(' One more number please, : '))
Color = num,Num
Color = led.fill(Gold,num,Num)
led.update()



