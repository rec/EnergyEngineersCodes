#This prompts the user for input and then flashes each letter individually.

from LEDsetup import*
#from flashA import*
#from flashB import*
#from flashC import*
#from flashD import*

#Turns lights off first
led.fill(Off)
led.update()


def flashA(color,TimeOn,TimeOff):
	a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
	for eachLED in a:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashB(color,TimeOn,TimeOff):
	b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
	for eachLED in b:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashC(color,TimeOn,TimeOff):
	c=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,47,57,67,77,76,66,72,71,62,61,51,41,31,21,11]
	for eachLED in c:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashD(color,TimeOn,TimeOff):
	d=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,47,51,57,66,61,71,72,73,74,75]
	for eachLED in d:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashE(color,TimeOn,TimeOff):
	e=[17,27,37,47,57,67,77,16,66,76,15,14,24,34,44,54,13,23,31,34,41,44,51,54,61,62,71,72,11,12,13,21,22,23,24]
	for eachLED in e:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashF(color,TimeOn,TimeOff):
	f=[11,12,13,14,15,16,17,21,22,23,24,34,44,54,27,37,47,57,67,77,76] 
	for eachLED in f:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashG(color,TimeOn,TimeOff):
	g=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,43,47,51,52,53,57,62,63,66,67,71,72,73,76,77]
	for eachLED in g:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashH(color,TimeOn,TimeOff):
	h=[17,27,16,26,15,25,14,24,13,23,12,22,11,21,34,44,54,64,74,67,77,66,76,65,75,64,74,63,73,62,72,61,71]
	for eachLED in h:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashI(color,TimeOn,TimeOff):
	i=[17,27,37,47,57,67,77,36,46,56,35,45,55,34,44,54,33,43,53,32,42,52,11,21,31,41,51,61,71]
	for eachLED in i:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashJ(color,TimeOn,TimeOff):
	j=[11,12,13,14,17,21,22,23,24,27,31,37,41,42,43,44,45,46,47,52,53,54,55,56,57,67,77]
	for eachLED in j:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashK(color,TimeOn,TimeOff):
	k=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,34,44,45,54,55,61,62,63,64,66,67,71,72,73,74,76,77]
	for eachLED in k:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
def flashL(color,TimeOn,TimeOff):
        l=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,62,71,72]
        for eachLED in l:
		led.set(eachLED,color)
        led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
def flashM(color,TimeOn,TimeOff):
        m=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,44,45,46,47,56,61,62,63,64,65,66,71,72,73,74,75,76]
        for eachLED in m:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashN(color,TimeOn,TimeOff):
        n=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,36,45,54,63,71,72,73,74,75,76,77]
        for eachLED in n:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)


def flashO(color,TimeOn,TimeOff):
        o=[12,13,14,15,16,21,22,23,24,25,26,27,31,36,37,41,47,51,57,61,57,72,73,74,75,76,67]
        for eachLED in o:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)


def flashP(color,TimeOn,TimeOff):
        p=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,54,57,64,65,66,67,74,75,76,77]
        for eachLED in p:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashQ(color,TimeOn,TimeOff):
        q=[12,13,14,15,16,21,22,23,24,25,26,27,31,37,41,43,47,51,52,57,60,61,62,63,64,65,66,67,70,71,73,74,75,76]
        for eachLED in q:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
    
def flashR(color,TimeOn,TimeOff):
        r=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,53,54,57,61,62,63,64,65,66,67,71,72,74,75,76]
        for eachLED in r:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashS(color,TimeOn,TimeOff):
        s=[17,27,37,47,57,67,77,16,26,66,76,15,25,14,24,34,44,54,64,63,73,62,72,12,22,11,21,31,41,51,61,71]
        for eachLED in s:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
def flashT(color,TimeOn,TimeOff):
        t=[17,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,52,53,54,55,56,57,67,77]
        for eachLED in t:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
def flashU(color,TimeOn,TimeOff):
        u=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,71,72,73,74,75,76,77]
        for eachLED in u:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashV(color,TimeOn,TimeOff):
        v=[17,27,67,77,16,26,66,76,15,25,55,65,14,24,54,64,13,23,43,53,12,22,42,52,11,21,31,41]
        for eachLED in v:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashW(color,TimeOn,TimeOff):
        w=[12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,41,42,43,44,51,52,61,62,63,64,65,67,72,73,74,75,76,77]
        for eachLED in w:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashW(color,TimeOn,TimeOff):
        w=[12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,41,42,43,44,51,52,61,62,63,64,65,67,72,73,74,75,76,77]
        for eachLED in w:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashX(color,TimeOn,TimeOff):
        x=[17,27,16,26,36,25,35,45,44,43,33,32,23,22,21,12,11,56,55,54,53,52,67,66,65,63,62,61,77,76,72,71,34]
        for eachLED in x:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashY(color,TimeOn,TimeOff):
        y=[15,16,17,21,24,25,26,27,31,34,41,44,51,54,61,62,63,64,65,66,67,71,72,73,74,75,76,77]
        for eachLED in y:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)

def flashZ(color,TimeOn,TimeOff):
        z=[17,27,37,47,67,77,57,16,26,56,66,76,45,55,24,34,44,54,64,43,33,12,22,32,62,72,11,21,31,41,51,61,71]
        for eachLED in z:
		led.set(eachLED,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
def flashSpace(color,TimeOn,TimeOff):
        led.fill(Off)
        led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
        

######################################################################################
######################################################################################

#need to define color, TimeOn, TimeOff. User will input these
color = Green
TimeOn = 0.4
TimeOff = TimeOn/2

input = raw_input('Please enter some text: ')
input = input.upper()

#inputColor = raw_input('Please enter a color: ')
#color = inputColor.capitalize()
#print color


TimeOn = raw_input('Please enter how long you want each character to flash: ')
TimeOn = float(TimeOn)


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' #these must be in the same order as the alphabetFunction list

alphabetFunction = [flashA,flashB,flashC,flashD,flashE,flashF,flashG,flashH,flashI,flashJ,flashK,flashL,flashM,flashN,flashO,flashP,flashQ,flashR,flashS,flashT,flashU,flashV,flashW,flashX,flashY,flashZ,flashSpace] #this is a list of functions that flash individual.

for character in input:
    for i in alphabet:
        if character == i:
           IndexNumber = alphabet.index(i) #returns index number of i in string alphabet
           flash = alphabetFunction[IndexNumber] #finds i-eth item in alphabetFunction
           flash(color,TimeOn,TimeOff)




    





