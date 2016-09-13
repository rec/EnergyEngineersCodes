from LEDsetup import*

led.fill(Off)
led.update()

def WESTarrow(color):
    westArrow=[65,66,67,68,69,51,71]
    for i in westArrow:
        led.set(i,color)
        led.update()
            

def eastarrow(color):
    EastArrow=[65,64,63,62,61,60,58,78]
    for  i in EastArrow:
        led.set(i,color)
        led.update()

def SouthArrow(color):
    southarrow=[65,54,45,34,25,14,5,15,13]
    for i in southarrow:
        led.set(i,color)
        led.update()
def NorthArrow(color):
    northarrow=[65,74,85,94,105,114,104,106]
    for i in northarrow:
        led.set(i,color)
        led.update()

def WLed(Color):
    w=[10,18,21,22,28,29,30,32,36,38,41,44,46,49,50,54,58,61,69,70,78,81,89]
    led.fill(Blue)
    led.update()
    for i in w:
        led.set(i,Color)
        led.update()
    return


def LedFlash():
    while True:
        WLed(Gold)
        time.sleep(0.2)
        led.fill(Off)
        led.update()
        time.sleep(0.2)
    return



        
        


Distance = int(raw_input('What is your current location? '))
Direction = raw_input('What direction you are going?  ')
print 'You are at your starting point.'

CL = Distance
pl = 10000
D = Direction

if D == 'N':
    NorthArrow(Purple)
    time.sleep(5)
elif D == 'E':
    eastarrow(White)
    time.sleep(5)
elif D == 'W':
    WESTarrow(Red)
    time.sleep(5)
elif D == 'S':
    SouthArrow(Yellow)
    time.sleep(5)

if CL<5:
    LedFlash()

elif CL<501:  
    if CL<pl:
        for blink in range(3):
            for i in range(0,256):
                led.fill((i,0,0))
                led.update()

        
elif CL>500 and CL<751:
    if CL<pl:
        for blink in range(3):
            for i in range(0,256):
                led.fill((i,i,0))
                led.update()

elif CL>750 and CL<1001:
    if CL<pl:
        for blink in range(3):
            for i in range(0,256):
               led.fill((0,i,0))
               led.update()

else:
    led.fill(Red)
    led.update()
    for i in range(255,-1,-1):
       led.fill((i,0,0))
       led.update()


#if CL<pl:
   #for blink in range(3):
    #for i in range(0,256):
           # led.fill((0,i,0))
          ##  led.update()
#
#else:
     #for i in range(255,-1,-1):
           ## led.fill((i,0,0))
           # led.update()
#WESTarrow(Green)
#eastarrow(Purple)
#SouthArrow(Pink)
#NorthArrow(Blue)


      
