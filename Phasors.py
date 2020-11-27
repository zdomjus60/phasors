import math

class Zee:

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0; self.y = 0;
            self.r = 0; self.phi = 0; self.z = (0,0)
            
        elif len(args) == 1:
            if isinstance(args[0], complex):
                self.x = args[0].real; self.y = args[0].imag
                self.r = 0; self.phi = 0; self.z = (0,0)
                self.to_polar()
                
        elif len(args) == 2:
            self.x = 0; self.y = 0
            self.r = args[0]; self.phi = args[1]
            self.z = (self.r, self.phi)
            self.to_rect()
                
    def to_rect(self):
        self.r = self.z[0]; self.phi = self.z[1]
        self.x = self.r * math.cos(math.radians(self.phi))      
        self.y = self.r * math.sin(math.radians(self.phi))
    
    def to_polar(self):
        self.r = math.sqrt(self.x*self.x + self.y*self.y) 
        self.phi = math.degrees(math.atan2(self.y, self.x))
        self.z = (self.r, self.phi)

    @property
    def ph(self):
        return (self.r, self.phi)

    @ph.setter
    def ph(self, value):
        if isinstance(value, tuple):
            self.z=value
            self.to_rect()

    @property
    def rect(self):
        return (self.x, self.y)

    @rect.setter
    def rect(self, value):
        if isinstance(value, complex):
            self.x = value.real; self.y = value.imag
            self.to_polar()

    def __add__(self, other):
        temp = Zee()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.to_polar()
        return temp

    def __sub__ (self, other):
        temp = Zee()
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        temp.to_polar()
        return temp
    
    def __mul__ (self, other):
        temp = Zee()
        temp.r = self.r * other.r
        temp.phi = self.phi + other.phi
        temp.z = (temp.r, temp.phi)
        temp.to_rect()
        return temp
    
    def __truediv__ (self, other):
        temp = Zee()
        temp.r = self.r / other.r
        temp.phi = self.phi - other.phi
        temp.z = (temp.r, temp.phi)
        temp.to_rect()
        return temp
    
    def series(self, other):
        temp = Zee()
        temp.x = self.x + other.x 
        temp.y = self.y + other.y
        temp.to_polar()
        return temp
    
    def parallel(self, other):
        temp1 = Zee()
        temp1.r = self.r * other.r 
        temp1.phi = self.phi + other.phi
        temp1.z = (temp1.r, temp1.phi)
        temp1.to_rect()
        
        temp2 = Zee()
        temp2.x = self.x + other.x
        temp2.y = self.y + other.y
        temp2.to_polar()
        
        temp = Zee()
        temp.r = temp1.r / temp2.r
        temp.phi = temp1.phi - temp2.phi
        temp.z = (temp.r, temp.phi)
        temp.to_rect()
        return temp
        
if __name__ == '__main__':
    f = Zee()
    f.rect = (11+9.5j)
    print(round(f.x,4), round(f.y,4), round(f.r,4), round(f.phi,4))

    print("-------------------")
    g = Zee()
    g.ph=(f.r, f.phi)
    print(round(g.x,4), round(g.y,4), round(g.r,4), round(g.phi,4))
    
    c = Zee(12,51) / Zee(3,-9)
    print(c.x, c.y, c.r, c.phi, c.z)
    
    
    