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
WESTarrow(Green)
eastarrow(Purple)
SouthArrow(Pink)
NorthArrow(Blue)


