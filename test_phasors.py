from Phasors import Zee

def summary(value):
    print(f"x:{value.x} y:{value.y} r:{value.r} phi:{value.phi}")

zL = Zee(0+5j)
zC = Zee(0-2j)
zR = Zee(10+0j)

zP = zL*zR/(zL+zR)
zT = zP+zC

i0 = Zee(50,30)/zT
v0 = i0*zC
summary(v0)

par = zL.parallel(zR)
summary(par)
