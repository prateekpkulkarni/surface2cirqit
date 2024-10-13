from flask import Flask, render_template, request, jsonify
from surface2cirqit import generate_surface_code_circuit, apply_logical_operation, SurfaceCode, SurfaceCodeError
from qiskit import QuantumCircuit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_circuit', methods=['POST'])
def generate_circuit():
    try:
        distance = int(request.form['distance'])
        circuit = generate_surface_code_circuit(distance)
        
        # Convert the circuit to a dictionary representation
        circuit_data = {
            'qubits': circuit.num_qubits,
            'depth': circuit.depth(),
            'instructions': [str(inst) for inst in circuit.data]
        }
        
        return jsonify({'success': True, 'circuit': circuit_data})
    except SurfaceCodeError as e:
        return jsonify({'success': False, 'error': str(e)})
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid distance value'})

@app.route('/apply_operation', methods=['POST'])
def apply_operation():
    try:
        distance = int(request.form['distance'])
        operation = request.form['operation']
        
        surface_code = SurfaceCode(distance)
        circuit = generate_surface_code_circuit(distance)
        apply_logical_operation(circuit, operation, surface_code)
        
        # Convert the circuit to a dictionary representation
        circuit_data = {
            'qubits': circuit.num_qubits,
            'depth': circuit.depth(),
            'instructions': [str(inst) for inst in circuit.data]
        }
        
        return jsonify({'success': True, 'circuit': circuit_data})
    except SurfaceCodeError as e:
        return jsonify({'success': False, 'error': str(e)})
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
