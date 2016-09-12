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


#need to define color, TimeOn, TimeOff. User will input these
color = Green
TimeOn = 0.075
#TimeOff = TimeOn/2



alphabet = 'A' #these must be in the same order as the alphabetFunction list

alphabetFunction = [scrollA]
for character in input:
    for i in alphabet:
        if character == i:
           IndexNumber = alphabet.index(i) #returns index number of i in string alphabet
           scroll = alphabetFunction[IndexNumber] #finds i-eth item in alphabetFunction
           scroll(color,TimeOn)




    





