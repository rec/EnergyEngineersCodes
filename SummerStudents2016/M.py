from LEDsetup import*
led.fill(Off)
led.update()

def M(color):
    m=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,44,45,46,47,56,61,62,63,64,65,66,71,72,73,74,75,76]
    for i in m:
            led.set(i,color)
            led.update()
    return
M(Crimson)
    
