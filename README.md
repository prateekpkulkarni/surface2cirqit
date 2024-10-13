# surface2cirqit
![Z29cq1R6](https://github.com/user-attachments/assets/7b0214df-b89c-4a53-8592-f596e4e74b83)
`surface2cirqit` is a high-precision Python package for generating quantum circuits for Surface Codes, designed to meet the exacting standards of advanced quantum error correction research.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Theory](#theory)
4. [API Reference](#api-reference)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)
8. [Citations](#citations)

## Installation

You can install `surface2cirqit` using pip:

```bash
pip install surface2cirqit
```

## Usage

Here's a basic example of how to use `surface2cirqit`:

```python
from surface2cirqit import generate_surface_code_circuit, SurfaceCode, apply_logical_operation

# Generate a Surface Code circuit with distance 3
circuit = generate_surface_code_circuit(3)

# Print the circuit
print(circuit)

# Apply a logical X operation
surface_code = SurfaceCode(3)
apply_logical_operation(circuit, 'X', surface_code)

# Print the modified circuit
print(circuit)
```

## Theory

Surface Codes are a class of quantum error correction codes that are particularly promising for fault-tolerant quantum computation. They are topological codes that encode logical qubits in the collective state of many physical qubits arranged on a 2D lattice.

Key features of Surface Codes:

1. **Topological Protection**: Surface Codes provide protection against local errors through their topological nature.

2. **High Threshold**: They have a relatively high error threshold, making them more resilient to noise.

3. **Planar Architecture**: Surface Codes can be implemented on a 2D lattice of qubits, making them suitable for many quantum computing architectures.

4. **Scalability**: The code distance can be increased by adding more physical qubits, allowing for arbitrarily low logical error rates.

The `surface2cirqit` package implements Surface Codes using the following components:

- **Data Qubits**: The physical qubits that encode the logical information.
- **Measure-X Qubits**: Ancilla qubits used to measure X-type stabilizers.
- **Measure-Z Qubits**: Ancilla qubits used to measure Z-type stabilizers.
- **Stabilizer Circuits**: Quantum circuits that implement the stabilizer measurements.

For a more detailed understanding of Surface Codes, please refer to the papers cited in the [Citations](#citations) section.

## API Reference

### Classes

#### `SurfaceCode`

Represents a Surface Code and provides methods to generate its quantum circuit.

- `__init__(distance: int)`: Initialize a Surface Code object.
- `generate_circuit() -> QuantumCircuit`: Generate the quantum circuit for the Surface Code.
- `apply_logical_x(circuit: QuantumCircuit) -> None`: Apply a logical X operation to the Surface Code circuit.
- `apply_logical_z(circuit: QuantumCircuit) -> None`: Apply a logical Z operation to the Surface Code circuit.

#### `SurfaceCodeError`

Custom exception class for Surface Code-related errors.

### Functions

#### `generate_surface_code_circuit(distance: int) -> QuantumCircuit`

Generate a quantum circuit for the Surface Code with the given distance.

#### `apply_logical_operation(circuit: QuantumCircuit, operation: str, surface_code: SurfaceCode) -> None`

Apply a logical operation to the Surface Code circuit.

## Examples

Here's an example of generating a Surface Code circuit and applying logical operations:

```python
from surface2cirqit import generate_surface_code_circuit, SurfaceCode, apply_logical_operation

# Generate a Surface Code circuit with distance 5
circuit = generate_surface_code_circuit(5)

# Create a SurfaceCode object
surface_code = SurfaceCode(5)

# Apply a logical X operation
apply_logical_operation(circuit, 'X', surface_code)

# Apply a logical Z operation
apply_logical_operation(circuit, 'Z', surface_code)

# Print the final circuit
print(circuit)
```

## Contributing

We welcome contributions to `surface2cirqit`! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and add tests if applicable
4. Run the test suite to ensure all tests pass
5. Submit a pull request with a clear description of your changes

For more detailed information, please see our [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citations

1. A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation," Physical Review A, vol. 86, no. 3, p. 032324, 2012. DOI: [10.1103/PhysRevA.86.032324](https://doi.org/10.1103/PhysRevA.86.032324)

2. Y. Tomita and K. M. Svore, "Low-distance surface codes under realistic quantum noise," Physical Review A, vol. 90, no. 6, p. 062320, 2014. DOI: [10.1103/PhysRevA.90.062320](https://doi.org/10.1103/PhysRevA.90.062320)

3. A. J. Landahl, J. T. Anderson, and P. R. Rice, "Fault-tolerant quantum computing with color codes," arXiv preprint arXiv:1108.5738, 2011. [arXiv:1108.5738](https://arxiv.org/abs/1108.5738)

4. S. B. Bravyi and A. Yu. Kitaev, "Quantum codes on a lattice with boundary," arXiv preprint quant-ph/9811052, 1998. [arXiv:quant-ph/9811052](https://arxiv.org/abs/quant-ph/9811052)

5. E. Dennis, A. Kitaev, A. Landahl, and J. Preskill, "Topological quantum memory," Journal of Mathematical Physics, vol. 43, no. 9, pp. 4452-4505, 2002. DOI: [10.1063/1.1499754](https://doi.org/10.1063/1.1499754)
