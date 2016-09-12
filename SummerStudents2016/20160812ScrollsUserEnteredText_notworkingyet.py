from LEDsetup import*

#Turns lights off first
led.fill(Off)
led.update()

a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
	for eachLED in a:
		led.set(eachLED,color)
	

def flashB(color,TimeOn,TimeOff):
	b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
	for eachLED in b:
		led.set(eachLED,color)

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


#######################

while True:
      letter = [6,16,5,15]

      counter = 0

      while counter < 90:
            for i in letter:
                  led.set(i + counter, Purple)
            led.update()
            time.sleep(0.1)
            led.fill(Off)
            led.update()
            counter = counter + 10
    





