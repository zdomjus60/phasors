
import json
from circuit_solver import Circuit
import math

# Define the frequency to use for the analysis.
# We used omega = 1 rad/s to calculate L and C, so f = omega / (2*pi).
analysis_freq = 1 / (2 * math.pi)

# Load the circuit description from the JSON file
with open('circuit_to_solve.json', 'r') as f:
    circuit_def = json.load(f)

# Create a circuit instance
my_circuit = Circuit(circuit_definition=circuit_def, frequency=analysis_freq)

# Generate the circuit diagram
my_circuit.draw_circuit("circuit_to_solve")

# Solve the circuit
try:
    node_voltages, v_source_currents = my_circuit.solve_nodal_analysis()

    # The equivalent impedance Zab is the voltage at node 1, because we used a 1A test source.
    Zab = node_voltages[1]

    print("--- Circuit Analysis Result ---")
    print(f"Equivalent Impedance (Zab): {Zab}")
    print(f"Rectangular form: {Zab.x:.4f} + j{Zab.y:.4f} Ω")
    print(f"Polar form: {Zab.r:.4f} ∠{Zab.phi:.2f}° Ω")

except Exception as e:
    print(f"An error occurred: {e}")
