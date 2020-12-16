import machine
import math
import utime

d = machine.DAC(machine.Pin(25))

for j in range(30):
    for i in range(0, 255):
        d.write(int(i))
        #utime.sleep_ms(2)        

