# Phasors

A Python library for AC circuit analysis using phasors.

## Features

-   Complex number representation with rectangular and polar coordinates.
-   Arithmetic operations (addition, subtraction, multiplication, division, power).
-   Representation of basic circuit components (Resistor, Inductor, Capacitor).
-   Voltage and Current sources.

## Installation

To get started, clone the repository:

```bash
git clone https://github.com/your-username/phasors.git
cd phasors
```

This project has no external dependencies beyond Python's standard library.

## Usage

Here's a quick example of how to use the `Phasors` library:

```python
from Phasors import Zee, Resistor, Inductor, Capacitor, VSource, ISource

# Create a phasor from rectangular coordinates
z1 = Zee(3, 4) # 3 + 4j
print(f"Z1: {z1}")

# Create a phasor from polar coordinates
z2 = Zee.from_polar(5, 90) # 5 at 90 degrees
print(f"Z2: {z2}")

# Perform arithmetic operations
z3 = z1 + z2
print(f"Z1 + Z2: {z3}")

# Calculate impedance of components
R = Resistor(100)
L = Inductor(0.1)
C = Capacitor(0.0001)

pulse = 2 * math.pi * 50 # 50 Hz

ZR = R.impedance(pulse)
ZL = L.impedance(pulse)
ZC = C.impedance(pulse)

print(f"Impedance of Resistor: {ZR}")
print(f"Impedance of Inductor: {ZL}")
print(f"Impedance of Capacitor: {ZC}")

# See more examples in examples.py
```

For more detailed examples, refer to the `examples.py` file.

## Running Tests

To run the unit tests for the project, use the following command:

```bash
python3 -m unittest test_suite.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
