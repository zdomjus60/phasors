from Phasors import *
import math

def current(t, phase):
    w = 1
    Im = 8.4
    return Im*math.cos(w*t/180.0*math.pi + math.radians(phase))



if __name__ == '__main__':
    
    for t in range(360):
        a = current(t, 0)
        b = current(t, 120)
        c = current(t,240)
        print(t, a+b+c)
        
        
        