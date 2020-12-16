import machine
import math
import utime

d = machine.DAC(machine.Pin(25))

for j in range(30):
    for i in range(0, 360):
        j = math.sin(math.radians(i))*125 + 128
        print(j)
        d.write(int(j))
        utime.sleep_ms(2)        

