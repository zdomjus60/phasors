# A Comprehensive Guide to AC Circuit Analysis with `phasors`

Welcome to the complete guide for the `phasors` library. This document is not just an API reference, but a full tutorial designed for anyone who wants to learn how to analyze alternating current (AC) electric circuits from the ground up.

## Part 1: The Fundamentals of Electrical Engineering and Phasors

Before diving into the code, it's essential to understand *why* this library is useful and the problems it solves. To do that, we need to take a step back and review some key concepts.

### Chapter 1: Introduction to Electric Circuits

An electric circuit is a closed path in which electric current can flow. You can imagine it like a water pipe system: the pipes are the wires, the water is the current, and the pressure pushing the water is the voltage.

#### Voltage, Current, and Resistance (DC)

In the simplest circuits, called direct current (DC) circuits, the flow of electrons is constant and moves in only one direction. The three main players are:

1.  **Voltage (V)**: Measured in **Volts (V)**. It is the "push" or "pressure" that makes the electrons move. It represents the electric potential difference between two points.
2.  **Current (I)**: Measured in **Amperes (A)**. It is the flow of electric charge—the number of electrons passing a point in a given amount of time.
3.  **Resistance (R)**: Measured in **Ohms (Ω)**. It is the opposition that the current encounters in its path. A resistor is a component designed to have a specific resistance.

These three quantities are linked by **Ohm's Law** [1], the most fundamental formula in electrical engineering:

`V = I * R`

This simple algebraic equation allows us to calculate any of the three quantities if we know the other two.

#### Deeper Dive: Kirchhoff's Laws and Basic Analysis

Ohm's law is powerful, but to analyze circuits with more than one component or more than one path, we need two additional principles, known as **Kirchhoff's Circuit Laws** [1, 2].

**Kirchhoff's Current Law (KCL)**

Also known as the "node law," KCL states that the algebraic sum of currents entering a node (a junction point) is equal to the sum of currents leaving it. In other words, charge does not accumulate at nodes: "what goes in must come out."

*Example:*
Imagine a node with three wires. If a current I1 = 3A flows in on the first wire, and I2 = 2A flows in on the second, then the current flowing out of the third wire, I3, must be `I3 = I1 + I2 = 5A`.

**Kirchhoff's Voltage Law (KVL)**

Also known as the "loop law," KVL states that the algebraic sum of the potential differences (voltages) around any closed path (or loop) in a circuit is equal to zero. This is a principle of energy conservation: if you start at one point, take a complete trip around a loop, and return to the same point, your electric potential must be the same.

*Example: The Voltage Divider*
Consider a 12V source connected in series with two resistors, R1 = 2Ω and R2 = 4Ω.
1.  The total resistance of the circuit is `R_total = R1 + R2 = 6Ω`.
2.  The total current flowing in the circuit (which is the same at every point in a series circuit) is `I = V / R_total = 12V / 6Ω = 2A`.
3.  The "voltage drop" across R1 is `V1 = I * R1 = 2A * 2Ω = 4V`.
4.  The voltage drop across R2 is `V2 = I * R2 = 2A * 4Ω = 8V`.
5.  According to KVL, the sum of the voltage supplied by the source must equal the sum of the voltage drops across the components: `12V = 4V + 8V`. The law holds.

This example leads directly to the **voltage divider formula**, a useful shortcut for calculating the voltage across a single resistor in a series without first calculating the current:

`V_Rx = V_total * (Rx / R_total)`

In our case, `V2 = 12V * (4Ω / 6Ω) = 12V * 0.666... = 8V`. The result is confirmed.

#### Power and Energy in DC

**Electric Power (P)** is the rate at which work is done by an electric current. It represents the speed at which energy is transferred or consumed. It is measured in **Watts (W)**.

The formulas for calculating the power dissipated by a resistor (usually as heat) are:
1.  `P = V * I` (Power = Voltage x Current)
2.  `P = I² * R` (derived from the first by substituting V with I*R)
3.  `P = V² / R` (derived from the first by substituting I with V/R)

In the previous example, the power dissipated by R2 is `P2 = V2 * I = 8V * 2A = 16W`.

**Energy (E)** is the power consumed or delivered over a period of time (t). It is measured in **Joules (J)**, where `1 Joule = 1 Watt * 1 second`. In common usage, for measuring electricity consumption, the **kilowatt-hour (kWh)** is often used, which is the energy consumed by a 1000W appliance running for one hour.

#### The Advent of Alternating Current (AC)

The electricity that comes into our homes is not direct current, but **alternating current (AC)**. Instead of flowing steadily in one direction, AC periodically reverses its polarity, oscillating back and forth. Its most common waveform is the **sine wave**.

A sine wave is described by:
*   **Amplitude (Vp)**: The maximum value (peak) of the wave.
*   **Frequency (f)**: Measured in **Hertz (Hz)**. It indicates how many complete oscillations occur in one second. In Europe, the standard frequency is 50 Hz; in the Americas, it is 60 Hz.
*   **Period (T)**: The time it takes to complete one full oscillation (`T = 1/f`).
*   **Phase (φ)**: Indicates the shift of the wave with respect to a reference point. A wave can be "leading" or "laging" another.

In AC circuits, two other fundamental components come into play besides resistors: **inductors** and **capacitors**. These components react to the *change* in voltage and current, and their behavior cannot be described by the simple Ohm's Law. This is where the problems begin.

### Chapter 2: The AC Circuit Problem and the Mathematical Solution

As mentioned, in AC, the behavior of inductors and capacitors depends on the *rate of change* of voltage and current. This introduces derivatives and integrals into our mathematical world.

*   Voltage across an inductor: `V(t) = L * dI(t)/dt`
*   Current through a capacitor: `I(t) = C * dV(t)/dt`

What happens when we use them in a circuit?

#### A Taste of Differential Equations

Let's imagine a simple RC series circuit powered by a voltage source Vg. According to Kirchhoff's Voltage Law (KVL), the sum of the voltages around the loop must be zero:

`Vg(t) - V_R(t) - V_C(t) = 0`

Substituting the component laws (`V_R = R*I`), we get:

`Vg(t) - R*I(t) - V_C(t) = 0`

But we also know that the current `I(t)` flowing through the circuit is the same current that charges the capacitor, so `I(t) = C * dV_C(t)/dt`. Substituting this as well, we get:

`Vg(t) - R*C*(dV_C/dt) - V_C(t) = 0`

Rearranging this, we arrive at a **first-order linear differential equation**:

`R*C*(dV_C/dt) + V_C(t) = Vg(t)`

This equation describes the voltage across the capacitor, `V_C(t)`, over time. If the source `Vg` is a sine wave (e.g., `Vg(t) = Vp * cos(ωt)`), the solution to this equation, while possible, requires specific mathematical techniques. For more complex circuits (with multiple loops and nodes), we would be faced with **systems of differential equations**, and their manual solution becomes extremely long, tedious, and error-prone.

**The motivation for an alternative method is clear**: we need a way to analyze AC circuits without having to solve differential equations every time. The solution is to transform the problem from the time domain to the **frequency domain**.

#### The Stroke of Genius: Using Complex Numbers

To avoid this mathematical nightmare, engineers and physicists adopted a powerful tool: **complex numbers**. The brilliant idea is to associate every sine wave with a complex number (which we will call a **phasor**), transforming the differential equations into simple algebraic equations.

A complex number is not "imaginary" in the sense of being fake. It is an extension of the number system that allows us to represent quantities on a two-dimensional plane. Instead of just the real number line, we have a plane. This is perfect for electrical engineering, where quantities have both a **magnitude** (a value) and a **phase** (an angle of displacement).

A complex number `z` is written as:

`z = a + jb`

*   `a` is the **real part**, its coordinate on the horizontal axis (the real axis).
*   `b` is the **imaginary part**, its coordinate on the vertical axis (the imaginary axis).
*   `j` is the **imaginary unit**, defined as `j = sqrt(-1)`. (In electrical engineering, `j` is used instead of `i` to avoid confusion with the symbol for current).

#### The Complex Plane and Operations

Visualizing complex numbers as vectors on the **Argand-Gauss plane** helps in understanding the operations:

**1. Rectangular and Polar Representations**
As we've seen, a vector on a plane can be described by its coordinates (a,b) or by its length and angle.
*   **Rectangular Form:** `z = a + jb`
*   **Polar Form:** `z = r∠φ`, where `r` is the magnitude and `φ` is the phase.

**2. Addition and Subtraction**
These are performed by separately adding or subtracting the real and imaginary parts. Graphically, this corresponds to the "parallelogram rule" for vector addition.
`(a + jb) + (c + jd) = (a+c) + j(b+d)`

**3. Multiplication and Division**
This is where the polar form shows its power. Given `z1 = r1∠φ1` and `z2 = r2∠φ2`:
*   **Multiplication:** `z1 * z2 = (r1 * r2) ∠ (φ1 + φ2)` (multiply the magnitudes, add the phases).
*   **Division:** `z1 / z2 = (r1 / r2) ∠ (φ1 - φ2)` (divide the magnitudes, subtract the phases).
Graphically, multiplying by a complex number `z` corresponds to scaling and rotating the original vector.

**4. Complex Conjugate**
The conjugate of `z = a + jb` is `z* = a - jb`. In polar form, if `z = r∠φ`, then `z* = r∠-φ`. The conjugate has the same real part and an opposite imaginary part. It is useful for rationalizing denominators and, as we will see, for power calculations.

#### Euler's Bridge: The Birth of Phasors

The formal mathematical link between sine waves and complex numbers is given by **Euler's Formula** [1]:

`e^(jφ) = cos(φ) + j*sin(φ)`

This identity is extraordinary. It tells us that an exponential with an imaginary argument is actually a complex number with a magnitude of 1. If we make the angle a function of time, `φ = ωt`, we get `e^(jωt) = cos(ωt) + j*sin(ωt)`. This expression describes a vector of length 1 rotating on the complex plane at an angular velocity `ω`.

Any sinusoid, `V(t) = Vp * cos(ωt + φ)`, can now be seen as the real part of a complex exponential:

`V(t) = Re{ Vp * e^(j(ωt + φ)) } = Re{ (Vp * e^(jφ)) * e^(jωt) }`

Let's analyze this expression:
*   `e^(jωt)`: This is the term that represents the rotation (the time dependency).
*   `Vp * e^(jφ)`: This is a complex number, constant in time, that "encodes" the amplitude `Vp` and the initial phase `φ`.

The brilliant idea of phasor analysis is this: since all signals in a linear circuit oscillate at the same frequency `ω`, we can **ignore the rotating term `e^(jωt)`** (which is common to all) and work only with the constant part, which holds the unique information about amplitude and phase.

This complex number, `**V** = Vp * e^(jφ) = Vp∠φ`, is the **phasor** associated with the sinusoid V(t).

We have completed the transformation: from a function of time `V(t)` to a static complex number `**V**`. We can now manipulate these numbers with complex algebra, a much simpler task than solving differential equations.

### Chapter 3: Phasors and Impedance

In the last chapter, we saw that AC circuits lead to differential equations and that complex numbers offer a way out. Here, we will formalize the use of phasors and impedance. This is where calculus is transformed into algebra.

#### From Differential Equations to Algebraic Equations

Let's revisit our RC circuit equation:

`R*C*(dV_C/dt) + V_C(t) = Vg(t)`

The core principle of phasor analysis is to assume that the source voltage `Vg(t)` is a sinusoid, and in a linear circuit, the response (all other voltages and currents, like `V_C(t)`) will also be sinusoids of the *same frequency*, differing only in amplitude and phase [1].

Let's represent our signals with their phasors:
*   `Vg(t) = Vp * cos(ωt + φ)` is represented by the phasor `**Vg** = Vp∠φ`.
*   `V_C(t)` is represented by the phasor `**Vc**`.

The magic trick lies in how differentiation in the time domain becomes multiplication in the frequency domain. If a time-domain signal `v(t)` corresponds to a phasor `**V**`, then its derivative `d(v(t))/dt` corresponds to the phasor `jω**V**`.

Why? The derivative of a sinusoid shifts its phase by +90° (a cosine becomes a -sine, which is a cosine shifted by +90°) and multiplies its amplitude by `ω`. In the complex plane, a +90° rotation is exactly what multiplication by `j` does.

Now, let's transform our differential equation term by term:
1.  `V_C(t)` becomes `**Vc**`.
2.  `dV_C/dt` becomes `jω**Vc**`.
3.  `Vg(t)` becomes `**Vg**`.

Substituting these into the equation gives us the phasor equation:

`RC * (jω**Vc**) + **Vc** = **Vg**`

We can now solve for `**Vc**` algebraically:

`**Vc** * (1 + jωRC) = **Vg**`
`**Vc** = **Vg** / (1 + jωRC)`

Look at what we've achieved! We found the phasor for the capacitor voltage, `**Vc**`, by performing a simple algebraic division. All information about `V_C(t)`'s amplitude and phase is contained in that complex number. This is profoundly simpler than solving the original differential equation.

#### Impedance (Z) and Admittance (Y)

This transformation leads us to generalize Ohm's Law for AC circuits. We define **Impedance (Z)** as the ratio of the voltage phasor to the current phasor for a component [1, 2].

`Z = **V** / **I**`  or  `**V** = Z * **I**`

Impedance is a complex number, measured in Ohms (Ω), that tells us two things:
*   Its magnitude `|Z|` is the ratio of voltage amplitude to current amplitude.
*   Its angle `∠Z` is the phase shift that the component introduces between voltage and current.

Let's formally derive the impedance for our three passive components:

1.  **Resistor (R):**
    *   The time-domain relationship is `v(t) = R*i(t)`. In the phasor domain, this is `**V** = R * **I**`.
    *   Therefore, `Z_R = **V** / **I** = R`.
    *   The impedance is purely real. The angle is 0°, so voltage and current are in phase.

2.  **Inductor (L):**
    *   The time-domain relationship is `v(t) = L * di(t)/dt`. In the phasor domain, this becomes `**V** = L * (jω**I**) = jωL * **I**`.
    *   Therefore, `Z_L = **V** / **I** = jωL`.
    *   The impedance is purely imaginary and positive. The angle is +90°, meaning voltage leads current by 90°.

3.  **Capacitor (C):**
    *   The time-domain relationship is `i(t) = C * dv(t)/dt`. In the phasor domain, `**I** = C * (jω**V**) = jωC * **V**`.
    *   To find impedance, we rearrange for `**V**/**I**`: `**V** / **I** = 1 / (jωC)`.
    *   Therefore, `Z_C = 1 / (jωC) = -j / (ωC)`.
    *   The impedance is purely imaginary and negative. The angle is -90°, meaning voltage lags current by 90°.

The inverse of impedance is **Admittance (Y)**, where `Y = 1/Z`. It is measured in Siemens (S) and is very useful for parallel connections.

#### Combining Impedances

Just like resistors in DC circuits, impedances can be combined.

**Series Combination:**
When impedances are in series, their values add up:
`Z_eq = Z1 + Z2 + ... + Zn`

*Example:* A 10Ω resistor in series with a 0.01H inductor at 50Hz (ω ≈ 314 rad/s).
`Z_R = 10 Ω`
`Z_L = j * 314 * 0.01 = j3.14 Ω`
`Z_eq = 10 + j3.14 Ω`

**Parallel Combination:**
When impedances are in parallel, their admittances add up. This leads to the familiar product-over-sum rule for two components:
`Z_eq = 1 / (1/Z1 + 1/Z2 + ... + 1/Zn)`
For two impedances: `Z_eq = (Z1 * Z2) / (Z1 + Z2)`

*Example:* A 10Ω resistor in parallel with a 100µF capacitor at 50Hz.
`Z_R = 10 Ω`
`Z_C = 1 / (j * 314 * 100e-6) = 1 / (j0.0314) = -j31.8 Ω`
`Z_eq = (10 * -j31.8) / (10 - j31.8) = -j318 / (10 - j31.8)`
To solve this, one would multiply the numerator and denominator by the conjugate of the denominator, or more easily, convert to polar form to perform the division.

#### Visualizing with Phasor Diagrams

A phasor diagram is a graph on the complex plane that shows the magnitude and phase relationships between the various voltages and currents in a circuit. It's a powerful visual tool.

*For single components (assuming current **I** is on the real axis at 0°):*
*   **Resistor:** **V_R** is aligned with **I**. They are in phase.
*   **Inductor:** **V_L** points straight up along the +j axis, 90° ahead of **I**.
*   **Capacitor:** **V_C** points straight down along the -j axis, 90° behind **I**.

*Example: RLC Series Circuit*
In a series circuit, the current **I** is the same through all components. We can use it as our reference phasor (placing it on the real axis).
*   The resistor voltage **V_R** is in phase with **I**.
*   The inductor voltage **V_L** leads **I** by 90°.
*   The capacitor voltage **V_C** lags **I** by 90°.
By KVL, the source voltage **Vs** must equal the vector sum of the individual voltage drops: `**Vs** = **V_R** + **V_L** + **V_C**`. The diagram would show these vectors added head-to-tail to equal the source voltage phasor.

This graphical addition makes it clear why, at resonance, **V_L** and **V_C** (which are equal and opposite vectors) cancel each other out, leaving **Vs** = **V_R**.

## Part 2: The `phasors` Library - Core Components

Now that we have a solid theoretical foundation, we can finally explore how the `phasors` library translates these concepts into working Python code. In this part, we will learn about the main classes and create the fundamental building blocks of any circuit.

### Chapter 4: First Steps with the Library

#### Environment Setup

The library is written in pure Python with only one external dependency, `numpy`, for solving linear systems. To get started, simply clone the repository and ensure `numpy` is installed.

```bash
# Clone the repository to a directory of your choice
git clone https://github.com/DomenicoMustara/phasors.git
cd phasors

# Install dependencies
pip install -r requirements.txt
```

#### Project Structure Overview

Before writing code, let's look at the main files that make up the project:

*   `Phasors.py`: This is the heart of the library. It contains the `Zee` class for managing complex numbers and the classes that define the basic components (`Resistor`, `Inductor`, `Capacitor`, `VSource`, `ISource`).
*   `circuit_solver.py`: This module contains the `Circuit` class, the engine that takes a circuit description as input, builds the system of equations (using Modified Nodal Analysis), and solves it to find voltages and currents.
*   `examples.py`: A valuable file containing several practical examples of how to use the library. It will be an excellent point of reference.
*   `circuit.json`: An example file showing how a circuit can be described in JSON format, a structured way to define components and connections.
*   `README.md`: The file you are currently reading, our complete guide.

Now that we have a map of the project, we are ready to explore the most important file: `Phasors.py`.

### Chapter 5: Defining Circuit Components: An API Deep Dive

All the logic for representing components and phasors is in the `Phasors.py` file. Let's analyze its classes in detail, treating this as a reference for the library's API.

#### The `Zee` Class: The Heart of Phasors

The `Zee` class is the library's implementation of a complex number, optimized for electrical calculations. It is the backbone of all frequency-domain operations.

##### Initialization

A `Zee` object can be created in several ways:

1.  **`Zee(x, y)`**: Creates a `Zee` object from rectangular (Cartesian) coordinates.
    *   `x` (float): The real part.
    *   `y` (float): The imaginary part.
    ```python
z1 = Zee(3, 4) # Represents 3 + j4
    ```
2.  **`Zee.from_polar(r, phi)`**: A class method to create a `Zee` object from polar coordinates. This is often the most intuitive way to define a phasor.
    *   `r` (float): The magnitude or modulus.
    *   `phi` (float): The phase angle in **degrees**.
    ```python
# Represents a phasor of magnitude 5 at an angle of 90 degrees
z2 = Zee.from_polar(5, 90)
    ```
3.  **`Zee.from_complex(c)`**: A class method to convert a standard Python `complex` number into a `Zee` object.
    ```python
c = 3 + 4j
z3 = Zee.from_complex(c)
    ```

##### Properties

Once created, you can access the number's representation in either form.

*   `.x`, `.y`: The rectangular coordinates.
*   `.r`, `.phi`: The polar coordinates (magnitude and phase in degrees).
*   `.rect`: A tuple `(x, y)`.
*   `.polar`: A tuple `(r, phi)`.

```python
z = Zee.from_polar(10, 53.13)
print(f"x = {z.x:.2f}, y = {z.y:.2f}") # Output: x = 6.00, y = 8.00
print(f"r = {z.r:.2f}, phi = {z.phi:.2f}°") # Output: r = 10.00, phi = 53.13°
```

##### Methods

*   **`.conjugate()`**: Returns the complex conjugate of the number. If `z = x + jy`, `z.conjugate()` returns `x - jy`.

##### Operator Overloading

The `Zee` class is powerful because its operators are overloaded to perform complex arithmetic naturally.

*   **`+`, `-` (Addition/Subtraction):**
    ```python
z1 = Zee(1, 2)
z2 = Zee(3, 1)
print(z1 + z2) # Output: x:4.00000 y:3.00000 | r:5.00000 ∠36.87°
    ```
*   **`*` (Multiplication):** Multiplies magnitudes and adds phases.
    ```python
z1 = Zee.from_polar(10, 30)
z2 = Zee.from_polar(2, 60)
print(z1 * z2) # Output: x:0.00000 y:20.00000 | r:20.00000 ∠90.00°
    ```
*   **`/` (Division):** Divides magnitudes and subtracts phases.
    ```python
z1 = Zee.from_polar(10, 30)
z2 = Zee.from_polar(2, 60)
print(z1 / z2) # Output: x:4.33013 y:-2.50000 | r:5.00000 ∠-30.00°
    ```
*   **`**` (Power):** Raises a complex number to a power.
    ```python
z = Zee(3, 4)
print(z ** 2) # (3+4j)^2 = -7 + 24j
    ```
*   **`//` (Parallel Impedance):** A custom operator to quickly calculate the equivalent impedance of two components in parallel. It computes `(z1 * z2) / (z1 + z2)`.
    ```python
Z1 = Zee(10, 0)  # 10 Ohm Resistor
Z2 = Zee(0, 10)  # j10 Ohm Inductor
Z_parallel = Z1 // Z2
print(Z_parallel) # Output: x:5.00000 y:5.00000 | r:7.07107 ∠45.00°
    ```

#### The Passive Component Classes

These classes represent physical components. Their main purpose is to calculate their impedance at a given frequency.

##### `Resistor(res)`
*   **`__init__(self, res)`**: `res` is the resistance in Ohms.
*   **`.resistance`**: A property to get or set the resistance value.
*   **`.impedance(pulse)`**: Returns the impedance (a `Zee` object). For a resistor, this is always `Zee(self.res, 0)`. The `pulse` argument is ignored but included for consistency.

##### `Inductor(ind)`
*   **`__init__(self, ind)`**: `ind` is the inductance in Henrys.
*   **`.inductance`**: A property to get or set the inductance value.
*   **`.impedance(pulse)`**: Returns the impedance `Z_L = jωL`.
    *   `pulse` (float): The angular frequency `ω` in rad/s.

##### `Capacitor(cap)`
*   **`__init__(self, cap)`**: `cap` is the capacitance in Farads.
*   **`.capacitance`**: A property to get or set the capacitance value.
*   **`.impedance(pulse)`**: Returns the impedance `Z_C = -j / (ωC)`.
    *   `pulse` (float): The angular frequency `ω` in rad/s.

#### The Source Classes: `VSource` and `ISource`

These classes represent ideal voltage and current sources. They inherit from `Zee`, so they are phasors themselves.

##### `VSource(voltage, frequency, phase)`
*   **`__init__(...)`**: 
    *   `voltage` (float): The RMS voltage value.
    *   `frequency` (float): The source frequency in Hz (defaults to 50.0).
    *   `phase` (float): The phase angle in degrees (defaults to 0).
*   The object itself is a `Zee` instance representing the voltage phasor.

##### `ISource(current, frequency, phase)`
*   **`__init__(...)`**: 
    *   `current` (float): The RMS current value.
    *   `frequency` (float): The source frequency in Hz (defaults to 50.0).
    *   `phase` (float): The phase angle in degrees (defaults to 0).
*   The object itself is a `Zee` instance representing the current phasor.

## Part 3: Building and Solving Circuits

### Chapter 6: Representing a Circuit

We have learned how to create individual components, but a circuit is made of components that are *connected* to each other. How can we communicate these connections to the library?

The library adopts a standard approach in circuit analysis, based on the concept of **nodes**.

A **node** is a point in a circuit where two or more components meet. To describe a network, we simply need to list all our components and specify which nodes they are connected to.

By convention:
*   **Node `0`** is always our reference point, or **ground**. Its voltage is, by definition, considered to be 0 Volts.
*   All other nodes are numbered with positive integers: `1`, `2`, `3`, ...

#### The Circuit Description Format

The library expects to receive the circuit topology as a **list of Python dictionaries**. Each dictionary in the list represents a single component and contains three key pieces of information:

1.  `"type"`: The type of component, as a string (e.g., `"Resistor"`, `"VSource"`).
2.  `"value"`: The value of the component. This is a number for R, L, and C, or a dictionary for sources (e.g., `{"voltage": 230, "phase": 0}`).
3.  `"nodes"`: A list of two integers `[node_1, node_2]` indicating the nodes the component is connected between.

#### Example: A Simple Voltage Divider

**Example Circuit:** A 10V source powers a 1kΩ resistor.

```
      R1 (1k)
   +----/\/\/\----+ 
   |              |
 V1 (+)           NODE 1
10V|              |
   -              |
   |              |
   +--------------+
   |
  NODE 0 (GND)
```
In this circuit:
*   The source `V1` is connected between node `1` and node `0`.
*   The resistor `R1` is also connected between node `1` and node `0`. They are in parallel.

Its Python representation will be:

```python
circuit_description = [
    {
        "type": "VSource",
        "value": {"voltage": 10, "phase": 0},
        "nodes": [1, 0]  # Connected between node 1 (positive) and node 0 (negative)
    },
    {
        "type": "Resistor",
        "value": 1000,
        "nodes": [1, 0]  # Connected between node 1 and node 0
    }
]
```

This list of dictionaries is all the solver needs. We can also save it in a `circuit.json` file to be loaded later.

Once we have defined our circuit's structure in this format, we are ready to feed it to the solver, as we will see in the next chapter.

### Chapter 7: The Automatic Solver

Now that we know how to describe a circuit, we are ready for the final step: solving it. This task is handled by the `Circuit` class found in the `circuit_solver.py` module.

#### The `Circuit` Class

This class is the analysis engine of the library. To use it, we must create an instance of it, providing it with the circuit description we prepared.


The constructor accepts two arguments:
1.  `circuit_definition`: the list of dictionaries describing the network topology.
2.  `frequency`: an optional argument that specifies the operating frequency (in Hz) for the entire circuit. If not provided, it defaults to 50 Hz.

#### The `.solve_nodal_analysis()` Method

Once the `Circuit` object is created, we can call its main method: `.solve_nodal_analysis()`.

This method does all the heavy lifting for us:
1.  It parses the list of components.
2.  It calculates the impedance of each component at the specified frequency.
3.  It builds the system of linear equations based on the **Modified Nodal Analysis (MNA)** technique.
4.  It uses the `numpy` library to solve the system of equations `Ax = b`, finding the unknowns of our circuit.


The method returns a tuple containing two dictionaries:
1.  `node_voltages`: A dictionary mapping each node number to the phasor (`Zee` object) of the voltage at that point with respect to node 0.
2.  `v_source_currents`: A dictionary mapping each voltage source to the phasor (`Zee` object) of the current flowing through it.

#### How it Works: A Look into Modified Nodal Analysis (MNA)

To understand what the solver is doing, we need to look at the algorithm it's based on: **Modified Nodal Analysis (MNA)** [2].

**1. Standard Nodal Analysis (NA)**

The foundation of MNA is standard Nodal Analysis. NA applies Kirchhoff's Current Law (KCL) at each node of a circuit (except for the ground node, which is our reference). For a circuit with `N` nodes, we get `N` equations. The unknowns in these equations are the node voltages. This can be expressed in a matrix form:

`G * V = I`

*   `V` is a vector of the `N` unknown node voltages.
*   `I` is a vector of the known currents being injected into the nodes by current sources.
*   `G` is the **admittance matrix**, which we build based on the components connected to each node. For example, a resistor `R` between node 1 and 2 (with admittance `Y = 1/R`) would add `Y` to the diagonal elements `G[1,1]` and `G[2,2]`, and subtract `Y` from the off-diagonal elements `G[1,2]` and `G[2,1]`.

**2. The Problem with Voltage Sources (Why "Modified"?)**

Standard NA works beautifully if a circuit only contains passive components and current sources. But what about ideal voltage sources? We can't use KCL directly, because we don't know in advance how much current is flowing *through* the voltage source. It's an unknown!

**3. The "Modification" in MNA**

MNA elegantly solves this problem by embracing the new unknown. It expands the set of equations to include not only the unknown node voltages but also the unknown currents flowing through the voltage sources.

Here's how it works:
1.  For every ideal voltage source in the circuit, we add its current as a new variable to our list of unknowns.
2.  To solve for this new variable, we need a new equation. That new equation is simply the definition of the voltage source itself! For a source `Vs` connected between node 1 (+) and node 2 (-), the new equation is `V1 - V2 = Vs`.

**4. The MNA Matrix Equation**

This process creates a larger, combined system of equations that can be represented in a block matrix form:

```
[
[ G | B ] [ V ]   [ I ]
[ - | - ] [ - ] = [ - ]
[ C | D ] [J_v]   [ E ]
]
```

*   The top-left `G` matrix is the same admittance matrix from standard NA.
*   The `V` vector contains the unknown node voltages.
*   The `J_v` vector is new: it contains the unknown currents for each voltage source.
*   The `B`, `C`, and `D` matrices describe the connections of the voltage sources. `B` and `C` map the voltage source currents into the KCL equations. `D` is zero for ideal voltage sources.
*   The `I` vector contains the known current sources, as before.
*   The `E` vector is new: it contains the known voltage values for each voltage source.

The `circuit_solver.py` script automatically builds these MNA matrices using the circuit description you provide. It then uses the powerful `numpy.linalg.solve()` function to solve this system for the unknown `V` and `J_v` vectors, which it then formats nicely into the dictionaries that are returned to you.

#### Complete Example: Solving Our First Circuit

Let's put it all together and solve the simple circuit defined in the previous chapter (10V source in parallel with a 1kΩ resistor).

```python
# Import the Circuit class from its module
from circuit_solver import Circuit
import math

# 1. Define the circuit description
circuit_description = [
    {
        "type": "VSource",
        "value": {"voltage": 10, "phase": 0},
        "nodes": [1, 0]
    },
    {
        "type": "Resistor",
        "value": 1000,
        "nodes": [1, 0]
    }
]

# 2. Create an instance of the circuit, specifying a 50 Hz frequency
# (although frequency is irrelevant for a purely resistive circuit)
my_circuit = Circuit(circuit_definition=circuit_description, frequency=50)

# 3. Call the solver
try:
    node_voltages, v_source_currents = my_circuit.solve_nodal_analysis()

    # 4. Analyze and print the results
    print("--- Circuit Analysis Complete ---")
    
    print("\nNode Voltages (Phasors):")
    for node, voltage in node_voltages.items():
        print(f"  - Voltage at Node {node}: {voltage}")

    print("\nCurrents through Voltage Sources:")
    for source_nodes, current in v_source_currents.items():
        print(f"  - Current in source between nodes {source_nodes}: {current}")

except Exception as e:
    print(f"An error occurred during circuit solution: {e}")
```

**Expected Output:**

```
--- Circuit Analysis Complete ---

Node Voltages (Phasors):
  - Voltage at Node 1: x:10.00000 y:0.00000 | r:10.00000 ∠0.00°
  - Voltage at Node 0: x:0.00000 y:0.00000 | r:0.00000 ∠0.00°

Currents through Voltage Sources:
  - Current in source between nodes (1, 0): x:0.01000 y:0.00000 | r:0.01000 ∠0.00°
```

As expected, the voltage at node 1 is exactly 10V at 0 degrees phase, identical to the source. The current through the source is `10V / 1000Ω = 0.01A` (10mA), also in phase.

We did it! We have built and solved our first circuit. Now we are ready to analyze more complex and realistic examples.

### Chapter 8: Complex Examples

Now that we are familiar with the workflow—define, solve, analyze—we can apply it to more interesting scenarios that highlight the true power of this approach.

#### Example 1: RLC Series Circuit and the Phenomenon of Resonance

An RLC series circuit is a fundamental testbed in electrical engineering. Let's analyze the following circuit:

**Circuit Diagram:**

```
      R1 (10Ω)     L1 (31.8mH)    C1 (318µF)
   +----/\/\/\----+----()()()----+----||----+
   |              |              |           |
 V1(+)          NODE 1         NODE 2        |
10V~
   |                                          |
   +------------------------------------------+
   |
  NODE 0 (GND)
```

We will use a frequency of **50 Hz**. At this frequency, and with the chosen values for L and C, their impedances (reactances) will be equal in magnitude but opposite in sign, a phenomenon known as **resonance**.

*   `Z_L = j * 2 * pi * 50 * 0.0318 ≈ +j10 Ω`
*   `Z_C = -j / (2 * pi * 50 * 0.000318) ≈ -j10 Ω`

In conditions of resonance, the impedance of the inductor and the capacitor cancel each other out. The circuit, as seen by the source, will behave as if only the resistor were present!

**Analysis Code:**

```python
from circuit_solver import Circuit
import math

# Operating frequency
freq = 50.0

# RLC Series Circuit Description
rlc_series_circuit = [
    {
        "type": "VSource",
        "value": {"voltage": 10, "phase": 0},
        "nodes": [1, 0]
    },
    {
        "type": "Resistor",
        "value": 10,
        "nodes": [1, 2] # Between node 1 and 2
    },
    {
        "type": "Inductor",
        "value": 0.0318,
        "nodes": [2, 3] # Between node 2 and 3
    },
    {
        "type": "Capacitor",
        "value": 0.000318,
        "nodes": [3, 0] # Between node 3 and 0
    }
]

# Create and solve the circuit
my_circuit = Circuit(circuit_definition=rlc_series_circuit, frequency=freq)
node_voltages, v_source_currents = my_circuit.solve_nodal_analysis()

# Print results
print("--- RLC Series Circuit Analysis (Resonance) ---")
print(f"\nFrequency: {freq} Hz")

print("\nNode Voltages:")
for node, voltage in node_voltages.items():
    print(f"  - V({node}): {voltage}")

print("\nSource Currents:")
for source_nodes, current in v_source_currents.items():
    print(f"  - I(V_source {source_nodes}): {current}")

# Calculate total current (same as current through R1)
# I_total = (V(1) - V(2)) / R1
I_total = (node_voltages[1] - node_voltages[2]) / 10
print(f"\nCalculated total circuit current: {I_total}")
```

**Analysis of Results:**

The program will print the voltages at nodes 1, 2, and 3. We will notice that:
1.  The voltage at node 1 (`V(1)`) is 10V, same as the source.
2.  The total current in the circuit will be `10V / 10Ω = 1A` in phase with the source voltage (`I_total ≈ 1∠0° A`), because the impedances of L and C have cancelled out.
3.  The voltage across the resistor (`V(1) - V(2)`) will be `1A * 10Ω = 10V`. Therefore, `V(2)` will be 0V.
4.  The voltage across the inductor (`V(2) - V(3)`) will be `1A * j10Ω = 10∠+90° V`. Therefore, `V(3)` will be `-10j V` (or `10∠-90° V`).
5.  The voltage across the capacitor (`V(3) - V(0)`) will be `1A * (-j10Ω) = 10∠-90° V`, which is exactly `V(3)`.

This example demonstrates how the solver correctly handles phases and how phasor analysis allows us to observe complex phenomena like resonance in an intuitive, algebraic way.

## Part 4: Advanced Topics and Appendices

We have covered all the main features of the library, from defining components to solving complex networks. In this final part, we look at a couple of useful techniques and conclude our guide.

### Chapter 9: AC Power Analysis

Solving for the voltage and current in a circuit is the first major step, but often the end goal is to determine how power is being used. In AC circuits, power is a more nuanced concept than in DC, and it's described by three related quantities: real, reactive, and complex power [1].

#### Complex Power (S)

The most complete representation of power in an AC circuit is **Complex Power (S)**. It's a complex number that contains all the power information for a component or a system.

It is calculated using the RMS voltage and current phasors. For a component with voltage phasor **V** and current phasor **I**, the complex power is:

`S = V * I*`

Where:
*   `V` is the RMS voltage phasor across the component.
*   `I*` is the **complex conjugate** of the RMS current phasor flowing through it.
*   **Note:** Using the conjugate of the current is the standard convention in power engineering. It ensures that the signs for reactive power work out correctly (positive for inductors, negative for capacitors).

Complex power `S` has a real part (P) and an imaginary part (Q):

`S = P + jQ`

Let's break down what these parts mean.

##### Real Power (P)
*   **What it is:** The real part of `S`. This is the "useful" power, representing the energy that is actually consumed by the circuit to perform work (like generating heat in a resistor, or turning a motor).
*   **Unit:** **Watts (W)**.
*   **Calculation:** `P = Re{S} = |V| * |I| * cos(θ)` where `θ` is the angle between the voltage and current phasors.

##### Reactive Power (Q)
*   **What it is:** The imaginary part of `S`. This is not "wasted" power, but rather power that is stored and then returned to the circuit by reactive components (inductors and capacitors). It "sloshes" back and forth between the source and the load, doing no real work, but the wires must still be able to carry the current associated with it.
*   **Unit:** **Volt-Amps Reactive (VAR)**.
*   **Calculation:** `Q = Im{S} = |V| * |I| * sin(θ)`.
*   **Sign Convention:** Inductive loads (like motors) *consume* reactive power, so they have a positive Q. Capacitive loads *supply* reactive power, so they have a negative Q.

##### Apparent Power (|S|)
*   **What it is:** The magnitude of the complex power vector `S`. This represents the "total" power that the circuit's wiring must be able to handle, including both the real and reactive components.
*   **Unit:** **Volt-Amps (VA)**.
*   **Calculation:** `|S| = sqrt(P² + Q²) = |V| * |I|`.

#### The Power Triangle and Power Factor (pf)

These three types of power form a right-angled triangle called the **Power Triangle**:
*   The adjacent side is **Real Power (P)**.
*   The opposite side is **Reactive Power (Q)**.
*   The hypotenuse is **Apparent Power (|S|)**.

The angle of this triangle is `θ`, the same as the phase angle of the load's impedance.

This leads to the **Power Factor (pf)**:

`pf = P / |S| = cos(θ)`

The power factor is a dimensionless number between 0 and 1 that measures a circuit's efficiency. A pf of 1.0 (or "unity") is ideal, meaning all power is real power (Q=0). A low power factor means a high amount of reactive power is flowing, which requires more current (and thus larger wires, etc.) to deliver the same amount of useful (real) power.

*   **Lagging pf:** Occurs in inductive circuits, where current *lags* voltage.
*   **Leading pf:** Occurs in capacitive circuits, where current *leads* voltage.

#### Power Calculation Example

Let's revisit the RLC circuit from Chapter 8 and calculate the power supplied by the source. We had `Vs = 10∠0° V` and the total current was `I_total ≈ 1∠0° A`.

**1. Calculate Complex Power (S):**
First, get the conjugate of the current phasor: `I* = 1∠-0° = 1∠0° A`.
`S = Vs * I* = (10∠0°) * (1∠0°) = 10∠0° VA`

**2. Find P and Q:**
In rectangular form, `S = 10 + j0`.
*   Real Power (P) = 10 W.
*   Reactive Power (Q) = 0 VAR.

**3. Find Apparent Power and Power Factor:**
*   Apparent Power |S| = 10 VA.
*   Power Factor (pf) = P / |S| = 10W / 10VA = 1.0.

This makes perfect sense! At resonance, the circuit behaves as purely resistive. The power factor is unity, and no reactive power is consumed.

**Code Example:**
```python
# Assuming `node_voltages` and `v_source_currents` are available from the solver
# from the RLC circuit in Chapter 8

# Source voltage phasor is at node 1
Vs = node_voltages[1] 

# Current from the source is found from the solver results
# Note: The solver returns current flowing OUT of the positive terminal, 
# which is what we need for power calculation (passive sign convention).
I_source = v_source_currents[tuple([1,0])] 

# Calculate complex power S = V * I*
S_source = Vs * I_source.conjugate()

print(f"\n--- Power Analysis ---")
print(f"Complex Power (S) supplied by source: {S_source}")
print(f"  - Real Power (P): {S_source.x:.2f} W")
print(f"  - Reactive Power (Q): {S_source.y:.2f} VAR")
print(f"  - Apparent Power (|S|): {S_source.r:.2f} VA")

# Power factor is cos(angle of S) or cos(angle of V - angle of I)
power_factor = S_source.x / S_source.r
print(f"  - Power Factor (pf): {power_factor:.2f}")
```

### Chapter 10: Final Remarks

#### Loading a Circuit from a JSON File

In our examples, we defined the circuit structure directly in Python code as a list of dictionaries. For greater flexibility, you can define the circuit in a separate `.json` file and load it dynamically.

This is useful for keeping the circuit definition (the "data") separate from the analysis logic (the "code").

Assume we have a file `my_circuit.json` with this content:
```json
[
    {
        "type": "VSource",
        "value": {"voltage": 10, "phase": 0},
        "nodes": [1, 0]
    },
    {
        "type": "Resistor",
        "value": 10,
        "nodes": [1, 0]
    }
]
```

We can load and analyze it with the following script:

```python
from circuit_solver import Circuit
import json

# Path to the file to load
json_file_path = 'my_circuit.json'
freq = 50.0

try:
    # Open and read the JSON file
    with open(json_file_path, 'r') as f:
        circuit_description = json.load(f)

    # From here, the process is identical to before
    my_circuit = Circuit(circuit_definition=circuit_description, frequency=freq)
    node_voltages, v_source_currents = my_circuit.solve_nodal_analysis()

    print(f"--- Analysis of circuit from {json_file_path} ---")
    print("\nNode Voltages:")
    for node, voltage in node_voltages.items():
        print(f"  - V({node}): {voltage}")

except FileNotFoundError:
    print(f"Error: file {json_file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

#### Idea for a Frequency Analysis (Bode Plot)

The library's structure makes it very easy to perform a frequency sweep, i.e., to study how a circuit's behavior changes as the source frequency varies.

Although the library does not have a built-in plotting function, you can implement such an analysis with a simple loop. The idea is to iterate over a range of frequencies, and for each one, solve the circuit and save the result of interest (e.g., the voltage at a specific node).

Here is some pseudo-code that illustrates the concept:

```python
# (after defining the circuit_description)
import numpy as np

# Define the range of frequencies to test (e.g., from 1 Hz to 1000 Hz)
frequencies_to_test = np.logspace(0, 3, num=100) # 100 points on a log scale
results = []

for freq in frequencies_to_test:
    # Create and solve the circuit at this specific frequency
    circuit = Circuit(circuit_definition=rlc_series_circuit, frequency=freq)
    node_voltages, _ = circuit.solve_nodal_analysis()
    
    # Save the result of interest (e.g., the magnitude of the voltage at node 2)
    output_voltage = node_voltages[2].r
    results.append(output_voltage)

# Now, 'results' contains the trend of the voltage as frequency changes
# and can be used to generate a plot (e.g., with matplotlib)
```

### Conclusion of the Guide

We have reached the end of our journey.

We started from the basic concepts of voltage and current, faced the complexity of AC circuits, and discovered how complex numbers and phasors provide an elegant mathematical shortcut.

We then translated this theory into practice using the `phasors` library. We learned to:
*   Represent phasors and impedances with the `Zee` class.
*   Create circuit components like `Resistor`, `Inductor`, and `Capacitor`.
*   Describe a network's topology using a node-based structure.
*   Use the `Circuit` class to automatically solve the circuit and obtain voltages and currents.

You now have all the knowledge needed to model and analyze a wide range of alternating current circuits. The next step is to experiment: try modeling circuits from textbooks, verify the results, and become confident with the tool. The `examples.py` file in the project is an excellent starting point for more examples.

Happy circuit analysis!

---

### Bibliography

[1] C. K. Alexander and M. N. O. Sadiku, *Fundamentals of Electric Circuits*, 6th ed., McGraw-Hill Education, 2017.
[2] J. W. Nilsson and S. A. Riedel, *Electric Circuits*, 11th ed., Pearson, 2019.

---

## Appendices

### Appendix A: Glossary

*   **Admittance (Y):** The inverse of impedance (`1/Z`), representing how easily a circuit allows current to flow. Measured in Siemens (S).
*   **Amplitude:** The peak value of a sinusoidal waveform from its center or zero point.
*   **Apparent Power (|S|):** The magnitude of the complex power vector (`|S| = |V_rms| * |I_rms|`). It represents the total power flowing in a circuit, including both real and reactive power. Measured in Volt-Amps (VA).
*   **Capacitor:** A passive component that stores energy in an electric field. Its impedance is imaginary and negative (`Zc = -j/(ωC)`).
*   **Complex Power (S):** A complex number (`S = P + jQ`) that provides a complete picture of the power in an AC circuit. Calculated as `S = V_rms * I_rms*`.
*   **Frequency (f):** The number of complete cycles an AC waveform completes per second. Measured in Hertz (Hz). `ω = 2πf`.
*   **Impedance (Z):** The total opposition to current flow in an AC circuit, comprising both resistance and reactance. It is a complex number measured in Ohms (Ω).
*   **Inductor:** A passive component that stores energy in a magnetic field. Its impedance is imaginary and positive (`Zl = jωL`).
*   **Kirchhoff's Laws (KCL/KVL):** Fundamental laws governing the conservation of charge (KCL) at nodes and energy (KVL) around loops in a circuit.
*   **Node:** A point in a circuit where two or more components are connected.
*   **Phasor:** A complex number used to represent the magnitude and phase of a sinusoidal signal at a specific frequency.
*   **Power Factor (pf):** The ratio of real power to apparent power (`pf = P / |S|`). It measures the efficiency of power transmission. A value of 1.0 is ideal.
*   **Reactance (X):** The imaginary part of impedance, representing the opposition to current from inductors (positive) and capacitors (negative).
*   **Real Power (P):** The average power consumed by a circuit to do useful work. Measured in Watts (W).
*   **Reactive Power (Q):** The power that "sloshes" back and forth between reactive components and the source. It does no real work. Measured in Volt-Amps Reactive (VAR).
*   **Resistor:** A passive component that dissipates energy, usually as heat. Its impedance is purely real.
*   **RMS (Root Mean Square):** The effective value of an AC signal. An AC voltage of a certain RMS value will deliver the same power to a resistor as a DC voltage of the same value. For a sinusoid, `V_rms = Vp / sqrt(2)`.