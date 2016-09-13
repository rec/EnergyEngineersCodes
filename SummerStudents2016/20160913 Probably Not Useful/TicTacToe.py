from LEDsetup import*

led.fill(Off)
led.update()


    


def TicTac(Color):
    tictac=[3,16,23,36,43,56,63,76,83,96,116,6,13,26,33,46,53,66,73,86,93,106,113,103]
    for i in tictac:
        led.set(i,Color)
        led.update()
        led.fill(Brown,70,79)
        led.fill(Brown,30,39)

def L(Color):
    l=[110,109,90,89,88,87,91,92,107,108,111,112]
    for i in l:
        led.set(i,Color)
        led.update()

def K(Color):
     k=[114,105,85,84,94,95,104,115]
     for i in k:
         led.set(i,Color)
         led.update()

def J(Color):
    J=[80,81,82,97,98,99,100,101,102,117,118,119]
    for i in J:
        led.set(i,Color)
        led.update()

def O(Color):
    O=[40,41,42,57,58,59,60,61,62]
    for i in O:
         led.set(i,Color)
         led.update()
def P (Color):
    P=[44,45,54,55,64,65]
    for i in P:
        led.set(i,Color)
        led.update()
def M (Color):
    M=[47,48,49,50,51,52,67,68,69]
    for i in M:
        led.set(i,Color)
        led.update()
            
def N (Color):
    N=[0,1,2,17,18,19,20,21,22]
    for i in N:
        led.set(i,Color)
        led.update()       
def R (Color):
    R=[4,5,14,15,24,25]
    for i in R:
        led.set(i,Color)
        led.update()
def S (Color):
    S=[7,8,9,10,11,12,27,28,29]
    for i in S:
        led.set(i,Color)
        led.update()
        
def Cat(Color):
    C=[90,26,27,28,29,37,38,41,42,56,57,58,81,82,106,107,108,109,89,98,99,97,102,101,30,49,50,69,70,33,52,67,72,93]
    for i in C:
        led.set(i,Color)
        led.update()
def W(Color):
    w=[20,39,40,100,99,80]
    for i in w:
        led.set(i,Color)
        led.update()
def Nose(Color):
    nose=[56,63,64,83,43,76,65,55,75,66]
    for i in nose:
        led.set(i,Color)
        led.update()
def Whiskers(Color):
    whiskers=[1,4,15,24,25,13,35,7,17,23,95,103,84,94,105,104,113,115,117]
    for i in whiskers:
        led.set(i,Color)
        led.update()







Cat(White)
W(Brown)
Nose(Pink)
Whiskers(Orange)
#TicTac(Brown)

#K(Pink)
#L(Red)
#J(Green)
#O(Yellow)
#P(Blue)
#M(Purple)
#N(Orange)
#R(White)
#S(Gray)
