from qiskit import QuantumCircuit
from qiskit.visualization import plot_circuit_layout
import matplotlib.pyplot as plt

# Create a new quantum circuit with two qubits
qc = QuantumCircuit(2)

# Add a Hadamard gate to qubit 0
qc.h(0)

# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)

# Draw the quantum circuit using Matplotlib
qc.draw("mpl")

# Show the circuit diagram
plt.show()
