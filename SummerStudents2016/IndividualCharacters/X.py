from LEDsetup import*
led.fill(Off)
led.update()

def X(color):
        x=[17,27,16,26,36,25,35,45,44,43,33,32,23,22,21,12,11,56,55,54,53,52,67,66,65,63,62,61,77,76,72,71,34]
        for i in x:
		led.set(i,color)
		led.update()

X (Gold)
