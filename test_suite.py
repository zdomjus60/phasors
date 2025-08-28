import unittest
from Phasors import Zee, Resistor, Inductor, Capacitor
import math

class TestZee(unittest.TestCase):

    def test_init_from_rect(self):
        z = Zee(3, 4)
        self.assertAlmostEqual(z.x, 3)
        self.assertAlmostEqual(z.y, 4)
        self.assertAlmostEqual(z.r, 5)
        self.assertAlmostEqual(z.phi, math.degrees(math.atan2(4, 3)))

    def test_init_from_polar(self):
        z = Zee.from_polar(5, 53.13)
        self.assertAlmostEqual(z.x, 3, places=2)
        self.assertAlmostEqual(z.y, 4, places=2)
        self.assertAlmostEqual(z.r, 5)
        self.assertAlmostEqual(z.phi, 53.13)

    def test_init_from_complex(self):
        z = Zee.from_complex(3+4j)
        self.assertAlmostEqual(z.x, 3)
        self.assertAlmostEqual(z.y, 4)
        self.assertAlmostEqual(z.r, 5)
        self.assertAlmostEqual(z.phi, math.degrees(math.atan2(4, 3)))

    def test_addition(self):
        z1 = Zee(1, 1)
        z2 = Zee(2, 3)
        z3 = z1 + z2
        self.assertAlmostEqual(z3.x, 3)
        self.assertAlmostEqual(z3.y, 4)

    def test_subtraction(self):
        z1 = Zee(2, 3)
        z2 = Zee(1, 1)
        z3 = z1 - z2
        self.assertAlmostEqual(z3.x, 1)
        self.assertAlmostEqual(z3.y, 2)

    def test_multiplication(self):
        z1 = Zee(1, 1)
        z2 = Zee(2, 3)
        z3 = z1 * z2
        # (1+j)(2+3j) = 2 + 3j + 2j + 3j^2 = 2 + 5j - 3 = -1 + 5j
        # This is wrong, multiplication is done in polar coordinates
        z1_polar = Zee(1,1).r, Zee(1,1).phi
        z2_polar = Zee(2,3).r, Zee(2,3).phi
        z3_polar_r = z1_polar[0] * z2_polar[0]
        z3_polar_phi = z1_polar[1] + z2_polar[1]
        z3_rect = Zee.from_polar(z3_polar_r, z3_polar_phi)
        self.assertAlmostEqual(z3.x, z3_rect.x)
        self.assertAlmostEqual(z3.y, z3_rect.y)

    def test_division(self):
        z1 = Zee(2, 3)
        z2 = Zee(1, 1)
        z3 = z1 / z2
        z1_polar = Zee(2,3).r, Zee(2,3).phi
        z2_polar = Zee(1,1).r, Zee(1,1).phi
        z3_polar_r = z1_polar[0] / z2_polar[0]
        z3_polar_phi = z1_polar[1] - z2_polar[1]
        z3_rect = Zee.from_polar(z3_polar_r, z3_polar_phi)
        self.assertAlmostEqual(z3.x, z3_rect.x)
        self.assertAlmostEqual(z3.y, z3_rect.y)

class TestResistor(unittest.TestCase):

    def test_impedance(self):
        r = Resistor(100)
        z = r.impedance(pulse=100) # pulse is not used for resistor
        self.assertAlmostEqual(z.x, 100)
        self.assertAlmostEqual(z.y, 0)

class TestInductor(unittest.TestCase):

    def test_impedance(self):
        l = Inductor(10)
        z = l.impedance(pulse=100)
        # Z = j*w*L = j*100*10 = 1000j
        self.assertAlmostEqual(z.x, 0)
        self.assertAlmostEqual(z.y, 1000)

class TestCapacitor(unittest.TestCase):

    def test_impedance(self):
        c = Capacitor(0.01)
        z = c.impedance(pulse=100)
        # Z = 1/(j*w*C) = -j/(w*C) = -j/(100*0.01) = -j
        self.assertAlmostEqual(z.x, 0)
        self.assertAlmostEqual(z.y, -1)

if __name__ == '__main__':
    unittest.main()