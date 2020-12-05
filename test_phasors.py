from Phasors import *
import math


#zL = Zee(0+5j)
#zC = Zee(0-2j)
#zR = Zee(10+0j)
#
#zP = zL*zR/(zL+zR)
#zT = zP+zC
#
#i0 = Zee(50,30)/zT
#v0 = i0*zC
#summary(v0)
#
#par = zL.parallel(zR)
#summary(par)

# Practice Problem 9.12
#za = Zee(0+4j)
#zb = Zee(0-3j)
#zc = Zee(8+5j)
#z4 = Zee(5-2j)
#z5 = Zee(10+0j)
#
#z1 = (zb*zc)/(za+zb+zc)
#z2 = (za*zc)/(za+zb+zc)
#z3 = (za*zb)/(za+zb+zc)
#
#ztot = z3+(z2.series(z4)).parallel(z1.series(z5))
#
#
#I = Zee(45,30)/ztot
#summary(I)

#Problem 9.13

#z2 = Zee(10-10j)
#z1 = Zee(0-10j)
#zC = z1//z2
#print("zC: ", end="")
#summary(zC)
#Vi = Zee(60, 0)
#R = Zee(10)
#V1 = Vi*zC/(zC+R)
#print("V1: ",end="")
#summary(V1)
#z3 = z1/(R+z1)
#summary(z3)
#summary(V1*z3)

# Esempio 9.15
#R3 = 1.5*10**6
#C3 = 12*10**(-12)
#f = 2000
#
#Z1 = 1000
#Z2 = 4200
#denom = f*2*math.pi*R3*C3
#denomj = 1+denom*1j
#
#Z3 = Zee(R3/(denomj))
#
#summary(Z3)
#
#Zx = Z3*Zee(Z2)/Zee(Z1)
#summary(Zx)

#Esempio 10.1
#V = Zee(20,0)
#R1 = Zee(10)
#H1 = Zee(4j)
#H2 = Zee(2j)
#C1 = Zee(-2.5j)

#i1 = Zee(1)/Zee(12+2j)
#print("I1: ", i1)
#v0 = Zee(-1)*i1 * Zee(8+4j)
#print("v0: ", v0)
#isum = Zee(0.2)*v0
#print("isum: ", isum)
#i2 = i1 - isum
#print("i2: ", i2)
#req = Zee(1)/i2
#print("req: ", req)
#ia = Zee(-32+16j)/Zee(12+2j)
#print("ia: ", ia)
#ib = Zee(8)+ia
#print("ib: ", ib)
#vth = ib*Zee(4-2j)+ia*Zee(8+4j)
#print("vth: ", vth)

#p1 = Zee(1,0)/(Zee(10000-2500j))
#print(p1)
#p2 = Zee(1)/(Zee(-5000j))
#print(p2)
#p3 = Zee(1)/Zee(10000)
#print(p3)
#v0 = p1/(p2-p3)
#print(v0)

# test rlc
r= Resistor(5)
i = Inductor(2)
c = Capacitor(2e-03)

zr = r.impedance(10)
zi = i.impedance(10)
zc = c.impedance(10)

print(zr)
print(zi)
print(zc)

print(zr, zi, zc)
