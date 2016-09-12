from LEDsetup import*
led.fill(Off)
led.update()


def T(color):
        t=[17,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,52,53,54,55,56,57,67,77]
	for i in t:
                led.set(i,color)
                led.update()
	return

T(Pink)




