from LEDsetup import*

RedLight = 0

while(RedLights<255):
    RedLights = RedLights + 25
    led.fill((RedLights,0,0))
    led.update()
