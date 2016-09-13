from LEDsetup import*
#Functions
def flashingGreen():
    led.fill(Off)
    led.update()
    count = 0
    while(count<4):
        count = count + 1
        led.fill(Green)
        led.update()
        time.sleep(0.3)
        led.update()
        led.fill(Off)
        led.update()
    return

def OneRow():
    led.set(0,Blue)
    led.update()
    return
def TwoRow():
    led.set(19,Pink)
    led.update()
    return
def ThreeRow():
    led.set(20,Red)
    led.update()
    return
def FourRow():
    led.set(39,White)
    led.update()
    return
def FiveRow():
    led.set(40,Green)
    led.update()
    return
def SixRow():
    led.set(59,Yellow)
    led.update()
    return

def SevenRow():
    led.set(60,Purple)
    led.update()
    return

def EightRow():
    led.set(79,Brown)
    led.update()
    return

def NineRow():
    led.set(80,Crimson)
    led.update()
    return
def TenRow():
    led.set(99,Purple)
    led.update()
    return
def ElevenRow():
    led.set(100,Gold)
    led.update()
    return
def TwelveRow():
    led.set(119,Maroon)
    led.update()
    return

def TopRowSet():
    TopRow=[0,19,20,39,40,59,60,79,80,99,100,119]
    for i in TopRow:
        led.set(i,Pink)
        led.update()
    return
def BottomRowSet():
    BottomRow=[9,10,29,30,49,50,69,70,89,90,109,110]
    for i in BottomRow:
        led.set(i,White)
        led.update()
    return


def RowSet(Row,Color):
    for i in Row:
        led.set(i,Color)
        led.update()
    return
TopRow=[0,19,20,39,40,59,60,79,80,99,100,119]
BottomRow=[9,10,29,30,49,50,69,70,89,90,109,110]
    

    

        







#Code Starts Here

#OneRow()
#TwoRow()
#ThreeRow()
#FourRow()
#FiveRow()
#SixRow()
#SevenRow()
#EightRow()
#NineRow()
#TenRow()
#ElevenRow()
#TwelveRow()
#TopRowSet()
#BottomRowSet()
RowSet(TopRow,Red)
RowSet(BottomRow,Green)



