from Phasors import *
import math

def main():
    # Problema 12.54
    Vp = Zee(210,0)
    Ia = Vp/Zee(80)
    Ib = Vp/Zee(60+90j)
    Ic = Vp/Zee(80j)
    print(f"Ia: {Ia}")
    print(f"Ib: {Ib}")
    print(f"Ic: {Ic}")
    print(f"In = {-Ia-Ib-Ic}")
    Sa = Vp*Ia.conjugate()
    print(f"Sa: {Sa}")
    Sb = Vp*Ib.conjugate()
    print(f"Sb: {Sb}")
    Sc = Vp*Ic.conjugate()
    print(f"Sc: {Sc}")
    S = Sa+Sb+Sc
    print(f"S: {S}")

if __name__ == "__main__":
    main()