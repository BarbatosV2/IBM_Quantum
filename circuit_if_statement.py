from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
 
qubits = QuantumRegister(1)
clbits = ClassicalRegister(1)
circuit = QuantumCircuit(qubits, clbits)
(q0,) = qubits
(c0,) = clbits
 
circuit.h(q0)
circuit.measure(q0, c0)
with circuit.if_test((c0, 1)):
    circuit.x(q0)
circuit.measure(q0, c0)
circuit.draw("mpl")
# example output counts: {'0': 1024}

#-------------------------------------------------------------------------------------------------#

qubits2 = QuantumRegister(2)
clbits2 = ClassicalRegister(2)
circuit2 = QuantumCircuit(qubits2, clbits2)
(q0, q1) = qubits2
(c0, c1) = clbits2
 
circuit2.h(q0)
circuit2.measure(q0, c0)
with circuit2.if_test((c0, 1)) as else_:
    circuit2.h(q1)
with else_:
    circuit2.x(q1)
circuit2.measure(q1, c1)
 
circuit2.draw("mpl")
# example output counts: {'01': 260, '11': 272, '10': 492}

#-------------------------------------------------------------------------------------------------#

qubits3 = QuantumRegister(3)
clbits3 = ClassicalRegister(3)
circuit3 = QuantumCircuit(qubits3, clbits3)
(q0, q1, q2) = qubits3
(c0, c1, c2) = clbits3
 
circuit3.h([q0, q1])
circuit3.measure(q0, c0)
circuit3.measure(q1, c1)
with circuit3.if_test((clbits3, 0b001)):
    circuit3.x(q2)
circuit3.measure(q2, c2)
 
circuit3.draw("mpl")
# example output counts: {'101': 269, '011': 260, '000': 252, '010': 243}

#-------------------------------------------------------------------------------------------------#

qubits4 = QuantumRegister(1)
clbits4 = ClassicalRegister(1)
circuit4 = QuantumCircuit(qubits4, clbits4)
(q0,) = qubits4
(c0,) = clbits4
 
circuit4.h(q0)
circuit4.measure(q0, c0)
with circuit4.switch(c0) as case:
    with case(0):
        circuit4.x(q0)
    with case(1):
        circuit4.z(q0)
circuit4.measure(q0, c0)
 
circuit4.draw("mpl")
 
# example output counts: {'1': 1024}

#-------------------------------------------------------------------------------------------------#

qubits5 = QuantumRegister(3)
clbits5 = ClassicalRegister(3)
circuit5 = QuantumCircuit(qubits5, clbits5)
(q0, q1, q2) = qubits5
(c0, c1, c2) = clbits5
 
circuit5.h([q0, q1])
circuit5.measure(q0, c0)
circuit5.measure(q1, c1)
with circuit5.switch(clbits5) as case:
    with case(0b000, 0b011):
        circuit5.z(q2)
    with case(0b001):
        circuit5.y(q2)
    with case(case.DEFAULT):
        circuit5.x(q2)
circuit5.measure(q2, c2)
 
circuit5.draw("mpl")
 
# example output counts: {'101': 267, '110': 249, '011': 265, '000': 243}

plt.show()