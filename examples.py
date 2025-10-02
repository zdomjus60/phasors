from Phasors import *
from circuit_solver import Circuit
import math

def nodal_analysis_example():
    print("\n--- Nodal Analysis Example (Parallel RC Circuit) ---")
    # Circuit: 1A current source in parallel with 10 Ohm Resistor and 0.01F Capacitor
    # Frequency: 50 Hz
    # Node 0: Ground
    # Node 1: Top node

    circuit_def = [
        {
            "type": "ISource",
            "value": {"current": 1, "phase": 0}, # 1A at 0 degrees
            "nodes": [0, 1] # From node 0 to node 1
        },
        {
            "type": "Resistor",
            "value": 10, # 10 Ohms
            "nodes": [1, 0]
        },
        {
            "type": "Capacitor",
            "value": 0.0001, # 0.0001 Farads
            "nodes": [1, 0]
        }
    ]

    circuit = Circuit(circuit_def, frequency=50.0)
    node_voltages, v_source_currents = circuit.solve_nodal_analysis()

    if node_voltages:
        print("Node Voltages:")
        for node, voltage in node_voltages.items():
            print(f"V_{node}: {voltage}")

def mna_example():
    print("\n--- MNA Example (Series RC Circuit with Voltage Source) ---")
    # Circuit: 10V Voltage Source in series with 10 Ohm Resistor and 0.0001F Capacitor
    # Frequency: 50 Hz
    # Node 0: Ground
    # Node 1: Between VSource and Resistor
    # Node 2: Between Resistor and Capacitor

    circuit_def = [
        {
            "type": "VSource",
            "value": {"voltage": 10, "frequency": 50, "phase": 0}, # 10V at 0 degrees
            "nodes": [0, 1] # From node 0 to node 1 (Node 1 is positive relative to Node 0)
        },
        {
            "type": "Resistor",
            "value": 10, # 10 Ohms
            "nodes": [1, 2]
        },
        {
            "type": "Capacitor",
            "value": 0.0001, # 0.0001 Farads
            "nodes": [2, 0]
        }
    ]

    circuit = Circuit(circuit_def, frequency=50.0)
    node_voltages, v_source_currents = circuit.solve_nodal_analysis()

    if node_voltages:
        print("Node Voltages:")
        for node, voltage in node_voltages.items():
            print(f"V_{node}: {voltage}")
    
    if v_source_currents:
        print("Currents through Voltage Sources:")
        # vs_nodes is now the tuple (n1, n2)
        for vs_nodes, current in v_source_currents.items():
            print(f"I_VSource (nodes {vs_nodes[0]}->{vs_nodes[1]}): {current}")

def main():
    # Problema 12.54
    Vp = Zee(210,0)
    Ia = Vp/Zee.from_complex(80)
    Ib = Vp/Zee.from_complex(60+90j)
    Ic = Vp/Zee.from_complex(80j)
    print(f"Ia: {Ia}")
    print(f"Ib: {Ib}")
    print(f"Ic: {Ic}")
    print(f"In = {-Ia-Ib-Ic}")
    Sa = Vp*Ia.conjugate()
    print(f"Sa: {Sa}")
    Sb = Vp*Ib.conjugate()
    print(f"Sb: {Sb}")
    Sc = Vp*Ic.conjugate()
    print(f"Sc: {Sc}")
    S = Sa+Sb+Sc
    print(f"S: {S}")

    nodal_analysis_example()
    mna_example()

if __name__ == "__main__":
    main()