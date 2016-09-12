from LEDsetup import*
from DataFunctions import*

led.fill(Off)
led.update()
time.sleep(1)

steps = 4

clrs = ColorScale(steps)

led.fill(clrs[0])
led.update()
time.sleep(1)
led.fill(clrs[1])
led.update()
time.sleep(1)
led.fill(clrs[2])
led.update()
time.sleep(1)
led.fill(clrs[3])
led.update()
time.sleep(1)



[timestamp, value] = OpenDailyData('Dunne_Daily_Max_2015_KWH.csv')
print(timestamp[0],value[0])
