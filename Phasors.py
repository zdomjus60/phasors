import math

class Zee(object):
    """A class to represent complex numbers and phasors."""

    def __init__(self, x=0, y=0):
        """Initializes a Zee object from rectangular coordinates."""
        self.x = x
        self.y = y
        self.to_polar()

    @classmethod
    def from_polar(cls, r, phi):
        """Creates a Zee object from polar coordinates."""
        x = r * math.cos(math.radians(phi))
        y = r * math.sin(math.radians(phi))
        return cls(x, y)

    @classmethod
    def from_complex(cls, c):
        """Creates a Zee object from a complex number."""
        return cls(c.real, c.imag)

    def to_rect(self):
        """Updates rectangular coordinates from polar coordinates."""
        self.x = self.r * math.cos(math.radians(self.phi))      
        self.y = self.r * math.sin(math.radians(self.phi))
    
    def to_polar(self):
        """Updates polar coordinates from rectangular coordinates."""
        self.r = math.sqrt(self.x*self.x + self.y*self.y) 
        self.phi = math.degrees(math.atan2(self.y, self.x))
    
    def conjugate(self):
        """Returns the conjugate of the complex number."""
        return Zee(self.x, -self.y)

    @property
    def polar(self):
        """Returns the polar representation (r, phi)."""
        return (self.r, self.phi)

    @property
    def rect(self):
        """Returns the rectangular representation (x, y)."""
        return (self.x, self.y)

    def __neg__(self):
        """Negates the complex number."""
        return Zee(-self.x, -self.y)

    def __add__(self, other):
        """Adds two complex numbers."""
        return Zee(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtracts two complex numbers."""
        return Zee(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        """Multiplies two complex numbers."""
        r = self.r * other.r
        phi = self.phi + other.phi
        return Zee.from_polar(r, phi)
    
    def __truediv__(self, other):
        """Divides two complex numbers."""
        r = self.r / other.r
        phi = self.phi - other.phi
        return Zee.from_polar(r, phi)

    def __pow__(self, other):
        """Raises a complex number to the power of another."""
        c = (self.x+self.y*1j)**(other.x+other.y*1j)
        return Zee.from_complex(c)
    
    def __floordiv__(self, other):
        """Calculates the parallel impedance."""
        return (self * other) / (self + other)

    def __str__(self):
        """Returns a string representation of the complex number."""
        # Normalize phi to be in the range (-180, 180]
        phi = self.phi
        if self.r < 0:
            self.r *= -1
            phi += 180.0
        while phi > 180.0:
            phi -= 360.0
        while phi <= -180.0:
            phi += 360.0
        return (f"x:{self.x:.5f} y:{self.y:.5f} | r:{self.r:.5f} ∠{phi:.2f}°")

        
class Resistor(Zee):
    """Represents a resistor in an AC circuit."""
    def __init__(self, res):
        """Initializes a Resistor object.

        Args:
            res (float): The resistance in Ohms.
        """
        super().__init__(res, 0)
        self.res = res
          
    @property
    def resistance(self):
        """The resistance of the resistor in Ohms."""
        return self.res
    
    @resistance.setter
    def resistance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.res = value
    
    def impedance(self, pulse):
        """Calculates the impedance of the resistor.

        Args:
            pulse (float): The angular frequency in rad/s.

        Returns:
            Zee: The impedance of the resistor.
        """
        return Zee(self.res, 0)

class Inductor(Zee):
    """Represents an inductor in an AC circuit."""
    
    def __init__(self, ind):
        """Initializes an Inductor object.

        Args:
            ind (float): The inductance in Henrys.
        """
        super().__init__()
        self.ind = ind
        
    @property
    def inductance(self):
        """The inductance of the inductor in Henrys."""
        return self.ind
    
    @inductance.setter
    def inductance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.ind = value

    def impedance(self, pulse):
        """Calculates the impedance of the inductor.

        Args:
            pulse (float): The angular frequency in rad/s.

        Returns:
            Zee: The impedance of the inductor.
        """
        return Zee(0, pulse * self.ind)
        
class Capacitor(Zee):
    """Represents a capacitor in an AC circuit."""
    
    def __init__(self, cap):
        """Initializes a Capacitor object.

        Args:
            cap (float): The capacitance in Farads.
        """
        super().__init__()
        self.cap = cap
        
    @property
    def capacitance(self):
        """The capacitance of the capacitor in Farads."""
        return self.cap
    
    @capacitance.setter
    def capacitance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                self.cap = value
        
    def impedance(self, pulse):
        """Calculates the impedance of the capacitor.

        Args:
            pulse (float): The angular frequency in rad/s.

        Returns:
            Zee: The impedance of the capacitor.
        """
        return Zee(0, -1/(pulse*self.cap))

class VSource(Zee):
    """Represents a voltage source in an AC circuit."""
    
    def __init__(self, voltage, frequency=50.0, phase=0):
        """Initializes a VSource object.

        Args:
            voltage (float): The voltage RMS value.
            frequency (float, optional): The frequency in Hz. Defaults to 50.0.
            phase (float, optional): The phase in degrees. Defaults to 0.
        """
        z = Zee.from_polar(voltage, phase)
        super().__init__(z.x, z.y)
        self.frequency = frequency
        self.pulse = self.frequency*2*math.pi
    
class ISource(Zee):
    """Represents a current source in an AC circuit."""
    
    def __init__(self, current, frequency=50.0, phase=0):
        """Initializes an ISource object.

        Args:
            current (float): The current RMS value.
            frequency (float, optional): The frequency in Hz. Defaults to 50.0.
            phase (float, optional): The phase in degrees. Defaults to 0.
        """
        z = Zee.from_polar(current, phase)
        super().__init__(z.x, z.y)
        self.frequency = frequency
        self.pulse = self.frequency*2*math.pi
