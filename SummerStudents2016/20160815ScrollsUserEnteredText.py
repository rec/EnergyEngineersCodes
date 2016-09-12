#This prompts the user for input and then flashes each letter individually. 

from LEDsetup import*

#Turns lights off first
led.fill(Off)
led.update()

# Here are the function definitions for each scrollable character.
def scrollA(color,TimeOn):
        a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
        counter = 90
        while counter > -90:
                for eachLED in a:
                        led.set(eachLED + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollB(color,TimeOn):
        b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
        counter = 90
        while counter > -90:
                for eachLED in b:
                        led.set(eachLED + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10



def scrollC(color,TimeOn):
        c=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,47,57,67,77,76,66,72,71,62,61,51,41,31,21,11]
        counter = 90
        while counter > -90:
                for eachLED in c:
                        led.set(eachLED + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollD (color,TimeOn):
        d=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,47,51,57,66,61,71,72,73,74,75]
        counter = 90
        while counter > -90:
                for eachLED  in d:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollE (color,TimeOn):
      e=[17,27,37,47,57,67,77,16,66,76,15,14,24,34,44,54,13,23,31,34,41,44,51,54,61,62,71,72,11,12,13,21,22,23,24]
      counter = 90
      while counter > -90:
        for eachLED  in e:
                led.set(eachLED  + counter,color)
        led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        counter = counter - 10

def scrollF (color,TimeOn):
        f=[11,12,13,14,15,16,17,21,22,23,24,34,44,54,27,37,47,57,67,77,76]
        counter = 90
        while counter > -90:
                for eachLED  in f:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollG (color,TimeOn):
        g=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,43,47,51,52,53,57,62,63,66,67,71,72,73,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in g:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollH (color,TimeOn):
        h=[17,27,16,26,15,25,14,24,13,23,12,22,11,21,34,44,54,64,74,67,77,66,76,65,75,64,74,63,73,62,72,61,71]
        counter = 90
        while counter > -90:
                for eachLED  in h:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollI (color,TimeOn):
        i=[17,27,37,47,57,67,77,36,46,56,35,45,55,34,44,54,33,43,53,32,42,52,11,21,31,41,51,61,71]
        counter = 90
        while counter > -90:
                for eachLED  in i:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollJ (color,TimeOn):
        j=[11,12,13,14,17,21,22,23,24,27,31,37,41,42,43,44,45,46,47,52,53,54,55,56,57,67,77]
        counter = 90
        while counter > -90:
                for eachLED  in j:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollK (color,TimeOn):
        k=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,34,44,45,54,55,61,62,63,64,66,67,71,72,73,74,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in k:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollL (color,TimeOn):
        l=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,62,71,72]
        counter = 90
        while counter > -90:
                for eachLED  in l:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollM (color,TimeOn):
        m=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,44,45,46,47,56,61,62,63,64,65,66,71,72,73,74,75,76]
        counter = 90
        while counter > -90:
                for eachLED  in k:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollN (color,TimeOn):
        n=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,36,45,54,63,71,72,73,74,75,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in n:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollO (color,TimeOn):
        o=[12,13,14,15,16,21,22,23,24,25,26,27,31,36,37,41,47,51,57,61,57,72,73,74,75,76,67]  
        counter = 90
        while counter > -90:
                for eachLED  in o:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollP (color,TimeOn):
        p=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,54,57,64,65,66,67,74,75,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in p:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollQ (color,TimeOn):
        q=[12,13,14,15,16,21,22,23,24,25,26,27,31,37,41,43,47,51,52,57,60,61,62,63,64,65,66,67,70,71,73,74,75,76]
        counter = 90
        while counter > -90:
                for eachLED  in q:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollR (color,TimeOn):
        r=[11,12,13,14,15,16,17,21,22,23,24,27,34,37,44,47,53,54,57,61,62,63,64,65,66,67,71,72,74,75,76]
        counter = 90
        while counter > -90:
                for eachLED  in k:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollS (color,TimeOn):
        s=[17,27,37,47,57,67,77,16,26,66,76,15,25,14,24,34,44,54,64,63,73,62,72,12,22,11,21,31,41,51,61,71]
        counter = 90
        while counter > -90:
                for eachLED  in s:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollT(color,TimeOn):
        t=[17,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,52,53,54,55,56,57,67,77]
        counter = 90
        while counter > -90:
                for eachLED  in t:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollU (color,TimeOn):
        u=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,41,51,61,71,72,73,74,75,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in u:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollV (color,TimeOn):
        v=[17,27,67,77,16,26,66,76,15,25,55,65,14,24,54,64,13,23,43,53,12,22,42,52,11,21,31,41]
        counter = 90
        while counter > -90:
                for eachLED  in v:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollW (color,TimeOn):
        w=[12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,41,42,43,44,51,52,61,62,63,64,65,67,72,73,74,75,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in w:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollX (color,TimeOn):
        x=[17,27,16,26,36,25,35,45,44,43,33,32,23,22,21,12,11,56,55,54,53,52,67,66,65,63,62,61,77,76,72,71,34]
        counter = 90
        while counter > -90:
                for eachLED  in x:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollY (color,TimeOn):
        y=[15,16,17,21,24,25,26,27,31,34,41,44,51,54,61,62,63,64,65,66,67,71,72,73,74,75,76,77]
        counter = 90
        while counter > -90:
                for eachLED  in y:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10
def scrollZ (color,TimeOn):
        z=[17,27,37,47,67,77,57,16,26,56,66,76,45,55,24,34,44,54,64,43,33,12,22,32,62,72,11,21,31,41,51,61,71]
        counter = 90
        while counter > -90:
                for eachLED  in z:
                        led.set(eachLED  + counter,color)
                led.update()
                time.sleep(TimeOn)
                led.fill(Off)
                led.update()
                counter = counter - 10

def scrollSpace(color,TimeOn):
        led.fill(Off)
        led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(1)


######################################################################################
######################################################################################

#need to define color, TimeOn, TimeOff. User will input these
color = Green
TimeOn = 0.075
#TimeOff = TimeOn/2

input = raw_input('Please enter some text: ')
input = input.upper()

#inputColor = raw_input('Please enter a color: ')
#color = inputColor.capitalize()
#print color


#TimeOn = raw_input('Please enter how quickly you want the letters to scroll(0.075 is a good starting point): ')
#TimeOn = float(TimeOn)


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' #these must be in the same order as the alphabetFunction list

alphabetFunction = [scrollA,scrollB,scrollC,scrollD,scrollE,scrollF,scrollG,scrollH,scrollI,scrollJ,scrollK,scrollL,scrollM,scrollN,scrollO,scrollP,scrollQ,scrollR,scrollS,scrollT,scrollU,scrollW,scrollX,scrollY,scrollZ,scrollSpace] #this is a list of functions that flash individual.

for character in input:
    for i in alphabet:
        if character == i:
           IndexNumber = alphabet.index(i) #returns index number of i in string alphabet
           scroll = alphabetFunction[IndexNumber] #finds i-eth item in alphabetFunction
           scroll(color,TimeOn)




    





