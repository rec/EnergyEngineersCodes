from LEDsetup import*

led.fill(Off)
led.update()

def I(color):
    i= [17,27,37,47,57,67,77,36,46,56,35,45,55,34,44,54,33,43,53,32,42,52,11,21,31,41,51,61,71]
    for s in i:
        led.set(s,color)
        led.update()
    return


def A(color):
	a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
	for i in a:
		led.set(i,color)
		led.update()
	return

def H(color):
    h = [17,27,16,26,15,25,14,24,13,23,12,22,11,21,34,44,54,64,74,67,77,66,76,65,75,64,74,63,73,62,72,61,71]
    for i in h:
        led.set(i,color)
        led.update()
    return

def D(color):
    d=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,47,51,57,66,61,71,72,73,74,75,76]
    for i in d:
        led.set(i,color)
        led.update()
    return

def B(color):
	b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
	for i in b:
		led.set(i,color)
		led.update()


led.fill(Off)
led.update()

H(Red)
time.sleep(0.3)
led.fill(Off)
led.update()
I(Blue)
time.sleep(2.5)
led.fill(Off)
led.update()
B(Yellow)
time.sleep(0.3)
led.fill(Off)
led.update()
A(Pink)
time.sleep(0.3)
led.fill(Off)
led.update()
D(White)
time.sleep(0.4)
led.fill(Off)
led.update()

led.fill(Off)
led.update()
