from LEDsetup import*
led.fill(Off)
led.update()

def J(Color):
        j=[11,12,13,14,17,21,22,23,24,27,31,37,41,42,43,44,45,46,47,52,53,54,55,56,57,67,77]
        for i in j:
            led.set(i,Color)
            led.update()
        return
J(Pink)
