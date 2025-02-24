from qiskit_ibm_runtime import QiskitRuntimeService

# Save IBM Quantum API token with the correct channel (only needed once)
QiskitRuntimeService.save_account(
    "Inserd_your_IBM_Quantumn_API_Token", 
    overwrite=True, 
    channel="ibm_quantum"  # 👈 This is required now
)

# Load the saved account
service = QiskitRuntimeService()

# List available quantum computers
print(service.backends())
