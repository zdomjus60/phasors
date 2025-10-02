## Rappresentazione del Circuito per l'Analisi

Per eseguire l'analisi circuitale utilizzando la classe `Circuit`, è necessario rappresentare il circuito tramite una **lista di dizionari**, dove ogni dizionario descrive un singolo componente del circuito.

### Struttura Generale di un Componente

Ogni dizionario componente deve avere almeno i seguenti campi:

*   `"type"`: Una stringa che specifica il tipo di componente (es. `"Resistor"`, `"Inductor"`, `"Capacitor"`, `"VSource"`, `"ISource"`).
*   `"nodes"`: Una lista di due interi `[nodo1, nodo2]`, che rappresentano i nodi a cui il componente è collegato. **Il nodo `0` è sempre considerato il nodo di massa (ground).**

### Campi Specifici per Tipo di Componente

#### 1. Resistor (Resistore)
*   `"value"`: Un float che indica la resistenza in Ohm.
    ```python
    {
        "type": "Resistor",
        "value": 100,  # 100 Ohm
        "nodes": [1, 2] # Collegato tra il nodo 1 e il nodo 2
    }
    ```

#### 2. Inductor (Induttore)
*   `"value"`: Un float che indica l'induttanza in Henry.
    ```python
    {
        "type": "Inductor",
        "value": 0.01, # 0.01 Henry
        "nodes": [2, 3]
    }
    ```

#### 3. Capacitor (Condensatore)
*   `"value"`: Un float che indica la capacità in Farad.
    ```python
    {
        "type": "Capacitor",
        "value": 1e-6, # 1 microFarad
        "nodes": [3, 0]
    }
    ```

#### 4. VSource (Sorgente di Tensione Indipendente)
*   `"value"`: Un dizionario con:
    *   `"voltage"`: float, l'ampiezza RMS della tensione in Volt.
    *   `"frequency"`: float, la frequenza in Hz (opzionale, se non specificata usa quella del circuito).
    *   `"phase"`: float, la fase in gradi (opzionale, default 0).
*   `"nodes"`: `[nodo_negativo, nodo_positivo]`. La tensione della sorgente è definita come `V_nodo_positivo - V_nodo_negativo`.
    ```python
    {
        "type": "VSource",
        "value": {"voltage": 12, "frequency": 50, "phase": 30}, # 12V RMS, 50Hz, 30 gradi di fase
        "nodes": [0, 1] # Il nodo 1 è a 12V rispetto al nodo 0 (massa)
    }
    ```

#### 5. ISource (Sorgente di Corrente Indipendente)
*   `"value"`: Un dizionario con:
    *   `"current"`: float, l'ampiezza RMS della corrente in Ampere.
    *   `"frequency"`: float, la frequenza in Hz (opzionale, se non specificata usa quella del circuito).
    *   `"phase"`: float, la fase in gradi (opzionale, default 0).
*   `"nodes"`: `[nodo_da_cui_esce, nodo_in_cui_entra]`. La corrente fluisce dal primo nodo al secondo.
    ```python
    {
        "type": "ISource",
        "value": {"current": 0.5, "phase": 45}, # 0.5A RMS, 45 gradi di fase
        "nodes": [1, 2] # La corrente fluisce dal nodo 1 al nodo 2
    }
    ```

### Come Utilizzare la Definizione del Circuito

Una volta creata la lista `circuit_definition`, la passi alla classe `Circuit`:

```python
from circuit_solver import Circuit

# Esempio di definizione di un circuito (la tua lista di dizionari)
my_circuit_definition = [
    # ... i tuoi componenti ...
    {
        "type": "Resistor",
        "value": 10,
        "nodes": [1, 0]
    },
    {
        "type": "ISource",
        "value": {"current": 1, "phase": 0},
        "nodes": [0, 1]
    }
]

# Frequenza operativa del circuito
circuit_frequency = 50.0 # Hz

# Crea un'istanza del circuito
circuit = Circuit(my_circuit_definition, frequency=circuit_frequency)

# Risolvi l'analisi nodale
node_voltages, v_source_currents = circuit.solve_nodal_analysis()

# Stampa i risultati
if node_voltages:
    print("Tensioni Nodali:")
    for node, voltage in node_voltages.items():
        print(f"V_{node}: {voltage}")

if v_source_currents:
    print("Correnti attraverso le Sorgenti di Tensione:")
    for nodes, current in v_source_currents.items():
        print(f"I_VSource (nodi {nodes[0]}->{nodes[1]}): {current}")
```

### Note Importanti:

*   **Nodo 0 (Ground):** È fondamentale che il circuito abbia un nodo di massa (ground), che è sempre il nodo `0`. Tutte le tensioni nodali sono calcolate rispetto a questo nodo.
*   **Frequenza:** La frequenza specificata nella creazione dell'oggetto `Circuit` è la frequenza operativa per tutti i componenti reattivi (induttori e condensatori) e per le sorgenti, se non specificato diversamente per la singola sorgente.
*   **Polarità/Direzione:** Fai attenzione alla direzione della corrente per le sorgenti di corrente e alla polarità per le sorgenti di tensione, poiché influenzano direttamente le equazioni MNA.
