from LEDsetup import*
led.fill(Off)
led.update()

def And (Color):
    nd =[37,47,26,56,25,35,55,34,44,23,53,73,22,32,62,21,31,41,51,71]
    for i in nd:
        led.set(i,Color)
        led.update()
    return
And(Violet)
