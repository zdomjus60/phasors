from Phasors import *
from circuit_solver import Circuit
import math
import json

def solve_simple_series_circuit():
    print("\n--- Simple Series Circuit Example (Voltage Source + Resistor) ---")
    # Circuit: 10V Voltage Source in series with 10 Ohm Resistor
    # Frequency: 50 Hz (arbitrary for DC-like circuit, but needed by the library)
    # Node 0: Ground
    # Node 1: Between VSource and Resistor

    with open('circuit.json', 'r') as f:
        circuit_def = json.load(f)

    circuit = Circuit(circuit_def, frequency=10.0 / (2 * math.pi))
    node_voltages, v_source_currents = circuit.solve_nodal_analysis()

    if node_voltages:
        print("Node Voltages:")
        for node, voltage in node_voltages.items():
            print(f"V_{node}: {voltage}")
    
    if v_source_currents:
        print("Currents through Voltage Sources:")
        for vs_nodes, current in v_source_currents.items():
            print(f"I_VSource (nodes {vs_nodes[0]}->{vs_nodes[1]}): {current}")

if __name__ == "__main__":
    solve_simple_series_circuit()
