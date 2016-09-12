# This program makes a square scroll left to right. Shizil dizil.

from LEDsetup import*
led.fill(Off)
led.update()


while True:
      a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]

      counter = 0

      while counter < 90:
            for i in a:
                  led.set(i + counter, Purple)
            led.update()
            time.sleep(0.2)
            led.fill(Off)
            led.update()
            counter = counter + 10
