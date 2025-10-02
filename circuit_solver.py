import numpy as np
from Phasors import Zee, Resistor, Inductor, Capacitor, VSource, ISource

class Circuit:
    """Represents an electrical circuit for nodal analysis."""
    def __init__(self, circuit_definition, frequency=50.0):
        """Initializes the Circuit with components and frequency.

        Args:
            circuit_definition (list): A list of dictionaries defining the circuit components.
            frequency (float, optional): The operating frequency of the circuit in Hz. Defaults to 50.0.
        """
        self.circuit_definition = circuit_definition
        self.frequency = frequency
        self.pulse = 2 * np.pi * self.frequency
        self.components = []
        self.nodes = set()
        self._parse_components()

    def _parse_components(self):
        """Parses the circuit definition and creates component objects."""
        for comp_def in self.circuit_definition:
            comp_type = comp_def["type"]
            comp_value = comp_def["value"]
            nodes = comp_def["nodes"]

            component = None
            if comp_type == "Resistor":
                component = Resistor(comp_value)
            elif comp_type == "Inductor":
                component = Inductor(comp_value)
            elif comp_type == "Capacitor":
                component = Capacitor(comp_value)
            elif comp_type == "VSource":
                component = VSource(comp_value["voltage"], self.frequency, comp_value["phase"])
            elif comp_type == "ISource":
                component = ISource(comp_value["current"], self.frequency, comp_value["phase"])
            
            if component:
                self.components.append({
                    "component": component,
                    "nodes": nodes,
                    "type": comp_type,
                    "polarity": comp_def.get("polarity", None) # For sources
                })
                self.nodes.update(nodes)

    def draw_circuit(self, filename="circuit"):
        """Generates a schematic diagram of the circuit using schemdraw."""
        try:
            import schemdraw
            import schemdraw.elements as elm
        except ImportError:
            print("Error: schemdraw is not installed.")
            print("Please install it with: pip install schemdraw")
            return

        # Helper to find a component by its nodes and type
        def find_comp(n1, n2, c_type):
            for c in self.components:
                if c['type'] == c_type and sorted(c['nodes']) == sorted([n1, n2]):
                    return c
            return None

        # There can be multiple components between two nodes.
        def find_comps(n1, n2):
            found = []
            for c in self.components:
                if sorted(c['nodes']) == sorted([n1, n2]):
                    found.append(c)
            return found

        with schemdraw.Drawing(unit=3.5, lw=2, fontsize=12) as d:
            # Manual layout for the specific circuit in circuit_to_solve.json
            
            # Node 1 components
            comps_1_0 = find_comps(1, 0)
            isource = next((c for c in comps_1_0 if c['type'] == 'ISource'), None)
            l1 = next((c for c in comps_1_0 if c['type'] == 'Inductor'), None)
            r1 = find_comp(1, 2, 'Resistor')
            c2 = find_comp(1, 4, 'Capacitor')

            # Node 2 components
            l2 = find_comp(2, 0, 'Inductor')
            c1 = find_comp(2, 3, 'Capacitor')

            # Node 3 components
            l3 = find_comp(3, 0, 'Inductor')
            r2 = find_comp(3, 4, 'Resistor')

            # Node 4 components
            l4 = find_comp(4, 0, 'Inductor')

            # Start drawing at Node 1
            if isource:
                d += elm.SourceI().up().label(f'{isource["component"].r}A', loc='top')
            d += (dot1 := elm.Dot().label('1', loc='bottom'))

            # Branch down to ground from node 1
            if l1:
                d.push()
                d += elm.Line().left(d.unit/4)
                d += elm.Inductor().down().label(f'{l1["component"].ind}H')
                d += elm.Ground()
                d.pop()

            # Horizontal path from 1 to 4
            if r1:
                d += elm.Resistor().right().label(f'{r1["component"].res}Ω')
            d += (dot2 := elm.Dot().label('2'))
            if l2:
                d.push()
                d += elm.Inductor().down().label(f'{l2["component"].ind}H')
                d += elm.Ground()
                d.pop()

            if c1:
                d += elm.Capacitor().right().label(f'{c1["component"].cap:.2f}F')
            d += (dot3 := elm.Dot().label('3'))
            if l3:
                d.push()
                d += elm.Inductor().down().label(f'{l3["component"].ind}H')
                d += elm.Ground()
                d.pop()

            if r2:
                d += elm.Resistor().right().label(f'{r2["component"].res}Ω')
            d += (dot4 := elm.Dot().label('4'))
            if l4:
                d.push()
                d += elm.Inductor().down().label(f'{l4["component"].ind}H')
                d += elm.Ground()
                d.pop()

            # Capacitor between 1 and 4, drawn above the main line
            if c2:
                d += elm.Line().at(dot1.start).up(d.unit/2)
                d += elm.Line().to((dot4.start.x, dot1.start.y + d.unit/2))
                d.add(elm.Capacitor().at(((dot1.start.x+dot4.start.x)/2, dot1.start.y+d.unit/2)).right().label(f'{c2["component"].cap}F'))
                d += elm.Line().at((dot4.start.x, dot1.start.y + d.unit/2)).to(dot4.start)

        try:
            d.save(f"{filename}.svg")
            print(f"Circuit diagram saved to {filename}.svg")
        except Exception as e:
            print(f"An error occurred while drawing the schematic: {e}")

    def solve_nodal_analysis(self):
        """Performs Modified Nodal Analysis (MNA) to find node voltages and currents through voltage sources.

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary mapping node numbers to their complex voltages (Zee objects).
                - dict: A dictionary mapping voltage source info (from self.components) to their complex currents (Zee objects).
        
        Raises:
            np.linalg.LinAlgError: If the system of equations cannot be solved.
        """
        # Identify non-ground nodes and voltage sources
        non_ground_nodes = sorted([n for n in list(self.nodes) if n != 0])
        voltage_sources = [comp for comp in self.components if comp["type"] == "VSource"]

        num_nodes = len(non_ground_nodes)
        num_v_sources = len(voltage_sources)
        total_eqs = num_nodes + num_v_sources

        # Map node numbers to matrix indices
        node_to_idx = {node: i for i, node in enumerate(non_ground_nodes)}
        
        # Map voltage source to matrix index (for current through source)
        v_source_map = {id(v_source): i for i, v_source in enumerate(voltage_sources)} # Use id() for unique key

        # Initialize MNA matrix and RHS vector
        MNA_matrix = np.zeros((total_eqs, total_eqs), dtype=complex)
        RHS_vector = np.zeros(total_eqs, dtype=complex)

        # Populate MNA matrix and RHS vector
        for comp_info in self.components:
            component = comp_info["component"]
            nodes = comp_info["nodes"]
            comp_type = comp_info["type"]
            polarity = comp_info["polarity"]

            n1, n2 = nodes[0], nodes[1] # Node 1 and Node 2 connected to the component

            # Get matrix indices, handling ground node (0)
            idx1 = node_to_idx[n1] if n1 != 0 else None
            idx2 = node_to_idx[n2] if n2 != 0 else None

            if comp_type in ["Resistor", "Inductor", "Capacitor"]:
                # Calculate admittance
                impedance = component.impedance(self.pulse)
                admittance = 1 / (impedance.x + 1j * impedance.y) # Convert Zee to complex for numpy

                # Apply to Y-matrix (top-left block)
                if idx1 is not None:
                    MNA_matrix[idx1][idx1] += admittance
                if idx2 is not None:
                    MNA_matrix[idx2][idx2] += admittance
                if idx1 is not None and idx2 is not None:
                    MNA_matrix[idx1][idx2] -= admittance
                    MNA_matrix[idx2][idx1] -= admittance
            elif comp_type == "ISource":
                # Current source contributes to RHS vector (top part)
                current_complex = component.x + 1j * component.y

                if idx1 is not None:
                    RHS_vector[idx1] -= current_complex # Current leaving n1
                if idx2 is not None:
                    RHS_vector[idx2] += current_complex # Current entering n2

            elif comp_type == "VSource":
                # Voltage source contributes to MNA matrix and RHS vector
                v_source_idx_in_mna = num_nodes + v_source_map[id(comp_info)] # Get index for this voltage source's current

                # Voltage equation: V_n2 - V_n1 = V_source (assuming n1 is negative, n2 is positive)
                if idx1 is not None:
                    MNA_matrix[v_source_idx_in_mna][idx1] = -1 # Coefficient for V_n1
                if idx2 is not None:
                    MNA_matrix[v_source_idx_in_mna][idx2] = 1  # Coefficient for V_n2
                RHS_vector[v_source_idx_in_mna] = component.x + 1j * component.y # Value of V_source

                # Current contribution to KCL equations
                if idx1 is not None:
                    MNA_matrix[idx1][v_source_idx_in_mna] = -1 # Current I_Vs leaves n1
                if idx2 is not None:
                    MNA_matrix[idx2][v_source_idx_in_mna] = 1  # Current I_Vs enters n2

        # Solve for node voltages and source currents
        try:
            solution_vector = np.linalg.solve(MNA_matrix, RHS_vector)
        except np.linalg.LinAlgError as e:
            print(f"Error solving system of equations: {e}")
            return None, None

        # Map results back to node voltages and source currents
        node_voltages = {node: Zee.from_complex(solution_vector[idx]) for node, idx in node_to_idx.items()}
        node_voltages[0] = Zee(0,0) # Ground node voltage is 0

        # Negate the current through the voltage source to represent current flowing OUT of the positive terminal
        v_source_currents = {tuple(v_source_info["nodes"]): -Zee.from_complex(solution_vector[num_nodes + v_source_map[id(v_source_info)]]) for v_source_info in voltage_sources}

        return node_voltages, v_source_currents