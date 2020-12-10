import math

class Zee(object):

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0; self.y = 0;
            self.r = 0; self.phi = 0; self.z = (0,0)
            
        elif len(args) == 1:
            if (isinstance(args[0], int)) or (isinstance(args[0], float)):
                self.x = args[0].real; self.y = 0
                self.r = args[0]; self.phi = 0; self.z = (self.r,0)
                
                
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
    
    def conjugate(self):
        temp = Zee()
        temp.phi = -self.phi
        temp.r = self.r
        temp.z = (temp.r, temp.phi)
        temp.to_rect()
        return temp

    @property
    def polar(self):
        return (self.r, self.phi)

    @polar.setter
    def polar(self, value):
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
            
    def __neg__(self):
        temp = Zee()
        temp.x = -self.x
        temp.y = -self.y
        temp.to_polar()
        return temp

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
    
    def __floordiv__(self, other):
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

    def __str__(self):
        if (self.r < 0):
            self.r *= -1
            self.phi += 180.0
        while self.phi > 360.0:
            self.phi -= 360.0
        while self.phi < -360.0:
            self.phi += 360.0
        self.x = float(self.x)
        self.y = float(self.y)
        self.r = float(self.r)
        self.phi=float(self.phi)
        return (f"x:{self.x:.5} y:{self.y:.5} r:{self.r:.5} phi:{self.phi:.5}")

        
class Resistor(Zee):
    def __init__(self, res):
        Zee.__init__(self)
        self.res = res
          
    @property
    def resistance(self):
        return self.res
    
    @resistance.setter
    def resistance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.res = value
    
    def impedance(self, pulse):
        self.x = self.r = self.res
        self.y = self.phi = 0
        return(self)

class Inductor(Zee):
    
    def __init__(self, ind):
        Zee.__init__(self)
        self.ind = ind
        
    @property
    def inductance(self):
        return self.ind
    
    @inductance.setter
    def inductance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.ind = value

    def impedance(self, pulse):
        self.x = 0
        self.y = self.r = pulse * self.ind
        self.phi = 90
        return(self)
        
class Capacitor(Zee):
    
    def __init__(self, cap):
        Zee.__init__(self)
        self.cap = cap
        
    @property
    def capacitance(self):
        return self.cap
    
    @capacitance.setter
    def capacitance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.cap = value
        
    def impedance(self, pulse):
        self.x = 0
        self.y = -1/pulse/self.cap
        self.r = 1/pulse/self.cap
        self.phi = -90
        return(self)

