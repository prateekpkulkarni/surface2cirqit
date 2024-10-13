"""
surface2cirqit: A package for generating quantum circuits for Surface Codes.

This module provides classes and functions to create and manipulate Surface Code
quantum circuits with high precision, suitable for advanced quantum error correction research.

Classes:
    SurfaceCode: Represents a Surface Code and provides methods to generate its quantum circuit.
    SurfaceCodeError: Custom exception class for Surface Code-related errors.

Functions:
    generate_surface_code_circuit: Generates a quantum circuit for a given Surface Code distance.
    apply_logical_operation: Applies a logical operation to the Surface Code circuit.
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister
from typing import List, Tuple, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SurfaceCodeError(Exception):
    """Custom exception class for Surface Code-related errors."""
    pass

class SurfaceCode:
    """
    Represents a Surface Code and provides methods to generate its quantum circuit.

    Attributes:
        distance (int): The distance of the Surface Code.
        num_qubits (int): Total number of qubits in the Surface Code.
        data_qubits (int): Number of data qubits.
        ancilla_qubits (int): Number of ancilla qubits.
        stabilizers (List[List[Tuple[int, int]]]): List of stabilizer operators.
    """

    def __init__(self, distance: int):
        """
        Initialize a Surface Code object.

        Args:
            distance (int): The distance of the Surface Code.

        Raises:
            SurfaceCodeError: If the distance is less than 3 or not an odd integer.
        """
        if distance < 3 or distance % 2 == 0:
            raise SurfaceCodeError("Surface Code distance must be an odd integer greater than or equal to 3.")
        
        self.distance = distance
        self.num_qubits = distance ** 2 + (distance - 1) ** 2
        self.data_qubits = distance ** 2
        self.ancilla_qubits = (distance - 1) ** 2
        self.stabilizers = self._generate_stabilizers()

        logger.info(f"Initialized Surface Code with distance {distance}")

    def _generate_stabilizers(self) -> List[List[Tuple[int, int]]]:
        """
        Generate the stabilizer operators for the Surface Code.

        Returns:
            List[List[Tuple[int, int]]]: List of stabilizer operators.
        """
        stabilizers = []
        
        # X-type stabilizers
        for i in range(self.distance - 1):
            for j in range(self.distance - 1):
                stabilizer = [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]
                stabilizers.append(stabilizer)
        
        # Z-type stabilizers
        for i in range(1, self.distance, 2):
            for j in range(1, self.distance, 2):
                stabilizer = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                stabilizers.append(stabilizer)
        
        return stabilizers

    def generate_circuit(self) -> QuantumCircuit:
        """
        Generate the quantum circuit for the Surface Code.

        Returns:
            QuantumCircuit: The generated quantum circuit for the Surface Code.
        """
        qr = QuantumRegister(self.num_qubits)
        circuit = QuantumCircuit(qr)

        # Initialize all data qubits to |+⟩ state
        for i in range(self.data_qubits):
            circuit.h(qr[i])

        # Apply stabilizer measurements
        for stabilizer in self.stabilizers:
            ancilla = self.data_qubits + self.stabilizers.index(stabilizer)
            
            if len(stabilizer) == 4:  # X-type stabilizer
                circuit.h(qr[ancilla])
                for qubit in stabilizer:
                    data = qubit[0] * self.distance + qubit[1]
                    circuit.cx(qr[data], qr[ancilla])
                circuit.h(qr[ancilla])
            else:  # Z-type stabilizer
                for qubit in stabilizer:
                    data = qubit[0] * self.distance + qubit[1]
                    circuit.cx(qr[ancilla], qr[data])

        logger.info("Generated Surface Code circuit")
        return circuit

    def apply_logical_x(self, circuit: QuantumCircuit) -> None:
        """
        Apply a logical X operation to the Surface Code circuit.

        Args:
            circuit (QuantumCircuit): The Surface Code circuit to modify.
        """
        for i in range(self.distance):
            circuit.x(i)
        logger.info("Applied logical X operation")

    def apply_logical_z(self, circuit: QuantumCircuit) -> None:
        """
        Apply a logical Z operation to the Surface Code circuit.

        Args:
            circuit (QuantumCircuit): The Surface Code circuit to modify.
        """
        for i in range(0, self.num_qubits, self.distance):
            circuit.z(i)
        logger.info("Applied logical Z operation")

def generate_surface_code_circuit(distance: int) -> QuantumCircuit:
    """
    Generate a quantum circuit for the Surface Code with the given distance.
    
    Args:
        distance (int): The distance of the Surface Code.
    
    Returns:
        QuantumCircuit: The generated quantum circuit for the Surface Code.
    
    Raises:
        SurfaceCodeError: If the distance is invalid.
    """
    try:
        surface_code = SurfaceCode(distance)
        return surface_code.generate_circuit()
    except SurfaceCodeError as e:
        logger.error(f"Failed to generate Surface Code circuit: {str(e)}")
        raise

def apply_logical_operation(circuit: QuantumCircuit, operation: str, surface_code: SurfaceCode) -> None:
    """
    Apply a logical operation to the Surface Code circuit.

    Args:
        circuit (QuantumCircuit): The Surface Code circuit to modify.
        operation (str): The logical operation to apply ('X' or 'Z').
        surface_code (SurfaceCode): The Surface Code object.

    Raises:
        ValueError: If an invalid operation is specified.
    """
    if operation.upper() == 'X':
        surface_code.apply_logical_x(circuit)
    elif operation.upper() == 'Z':
        surface_code.apply_logical_z(circuit)
    else:
        raise ValueError("Invalid logical operation. Use 'X' or 'Z'.")

if __name__ == "__main__":
    # Example usage
    try:
        distance = 3
        circuit = generate_surface_code_circuit(distance)
        print(f"Generated Surface Code circuit with distance {distance}:")
        print(circuit)

        # Apply a logical X operation
        surface_code = SurfaceCode(distance)
        apply_logical_operation(circuit, 'X', surface_code)
        print("\nCircuit after applying logical X operation:")
        print(circuit)
    except SurfaceCodeError as e:
        print(f"Error: {str(e)}")
