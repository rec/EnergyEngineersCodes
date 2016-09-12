from LEDsetup import*
led.fill(Off)
led.update()

def O(Color):
    o=[12,13,14,15,16,21,22,23,24,25,26,27,31,36,37,41,47,51,57,61,57,72,73,74,75,76,67]
    for i in o:
            led.set(i,Color)
            led.update()
    return
O(Green)
