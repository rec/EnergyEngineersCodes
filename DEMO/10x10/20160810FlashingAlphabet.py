#This program flashes each letter of the alphabet, A through Z.

from LEDsetup import*
led.fill(Off)
led.update()

color = Pink

flashtime = 1.0


def flash_A(color):
    a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
    for i in a:
        led.set(i,color)
        led.update()
        time.sleep(flashtime)
flash_A(color)


def flash_B(color):
    b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
    for i in b:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_B(color)


def flash_C(color):
    c=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,47,57,67,77,76,66,72,71,62,61,51,41,31,21,11]
    for i in c:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_C(color)


def flash_D(color):
    d=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,47,51,57,66,61,71,72,73,74,75]
    for i in d:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_D(color)


def flash_E(color):
    e=[17,27,37,47,57,67,77,16,66,76,15,14,24,34,44,54,13,23,31,34,41,44,51,54,61,62,71,72,11,12,13,21,22,23,24]
    for i in e:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_E(color)


def flash_F(color):
   f = [11,12,13,14,15,16,17,21,22,23,24,34,44,54,27,37,47,57,67,77,76] 
   for i in f:
        led.set(i,color)#missing a pixel
   led.update()
   time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_F(color)



def flash_G(color):
   g = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,43,47,51,52,53,57,62,63,66,67,71,72,73,76,77]
   for i in g:
        led.set(i,color)
   led.update()
   time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_G(color)



def flash_H(color):
   h = [17,27,16,26,15,25,14,24,13,23,12,22,11,21,34,44,54,64,74,67,77,66,76,65,75,64,74,63,73,62,72,61,71]
   for i in h:
        led.set(i,color)
   led.update()
   time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_H(color)



def flash_I(color):
   i= [17,27,37,47,57,67,77,36,46,56,35,45,55,34,44,54,33,43,53,32,42,52,11,21,31,41,51,61,71]
   for i in i:
        led.set(i,color)
   led.update()
   time.sleep(flashtime)
   
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_I(color)




def flash_J(color):
        j=[11,12,13,14,17,21,22,23,24,27,31,37,41,42,43,44,45,46,47,52,53,54,55,56,57,67,77]
        for i in j:
                led.set(i,color)
        led.update()
        time.sleep(flashtime)
        

#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_J(color)


def flash_K(color):
    k=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,34,44,45,54,55,61,62,63,64,66,67,71,72,73,74,76,77]
    for i in k:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_K(color)



def flash_L(color):
    l=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,62,71,72]
    for i in l:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
#led.fill(Off)
#led.update()
#time.sleep(1.5)
flash_L(color)



def flash_M(color):
    m=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,44,45,46,47,56,61,62,63,64,65,66,71,72,73,74,75,76]
    for i in m:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_M(color)



def flash_N(color):
        n = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,36,45,54,63,71,72,73,74,75,76,77]
        for i in n:
                led.set(i,color)
        led.update()
        time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_N(color)



def flash_O(color):
    o=[12,13,14,15,16,21,22,23,24,25,26,27,31,36,37,41,47,51,57,61,57,72,73,74,75,76,67]
    for i in o:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)   
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_O(color)



def flash_P(color):
    p=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,54,57,64,65,66,67,74,75,76,77]
    for i in p:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_P(color)



def flash_Q(color):
    q=[12,13,14,15,16,21,22,23,24,25,26,27,31,37,41,43,47,51,52,57,60,61,62,63,64,65,66,67,70,71,73,74,75,76]
    for i in q:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_Q(color)


def flash_R (color):
    r=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,53,54,57,61,62,63,64,65,66,67,71,72,74,75,76]
    for i in r:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_R(color)



def flash_S(color):
        s=[17,27,37,47,57,67,77,16,26,66,76,15,25,14,24,34,44,54,64,63,73,62,72,12,22,11,21,31,41,51,61,71]
        for i in s:
                led.set(i,color)
        led.update()
        time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_S(color)



def flash_T(color):
        t=[17,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,52,53,54,55,56,57,67,77]
	for i in t:
            led.set(i,color)
            led.update()
            time.sleep(flashtime)
	
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_T(color)



def flash_U(color):
    u=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,71,72,73,74,75,76,77]
    for i in u:
            led.set(i,color)
    led.update()
    time.sleep(flashtime)
    
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_U(color)



def flash_V(color):
        v=[17,27,67,77,16,26,66,76,15,25,55,65,14,24,54,64,13,23,43,53,12,22,42,52,11,21,31,41 ]
        for i in v:
                led.set(i,color)
        led.update()
        time.sleep(flashtime)

#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_V(color)



def flash_W (color):
    w=[12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,41,42,43,44,51,52,61,62,63,64,65,67,72,73,74,75,76,77]
    for i in w:
        led.set (i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(0.75)
flash_W(color)


def flash_X(color):
        x=[17,27,16,26,36,25,35,45,44,43,33,32,23,22,21,12,11,56,55,54,53,52,67,66,65,63,62,61,77,76,72,71,34]
        for i in x:
                led.set(i,color)
        led.update()
        time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_X(color)




def flash_Y(color):
    y=[15,16,17,21,24,25,26,27,31,34,41,44,51,54,61,62,63,64,65,66,67,71,72,73,74,75,76,77]
    for i in y:
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)
flash_Y(color)



def flash_Z (color):
    z=[17,27,37,47,67,77,57,16,26,56,66,76,45,55,24,34,44,54,64,43,33,12,22,32,62,72,11,21,31,41,51,61,71]
    for i in z :
        led.set(i,color)
    led.update()
    time.sleep(flashtime)
#time.sleep(2)
led.fill(Off)
led.update()
time.sleep(1.5)

flash_Z(color)








