from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)


def calculate(operation, a, b=None):
    if operation == 'add':
        return a + b
    if operation == 'subtract':
        return a - b
    if operation == 'multiply':
        return a * b
    if operation == 'divide':
        if b == 0:
            raise ValueError('Division by zero is not allowed')
        return a / b
    if operation == 'power':
        return a ** b
    if operation == 'modulus':
        if b == 0:
            raise ValueError('Modulus by zero is not allowed')
        return a % b
    if operation == 'sqrt':
        if a < 0:
            raise ValueError('Square root of a negative number is not allowed')
        return math.sqrt(a)
    raise ValueError(f'Unsupported operation: {operation}')


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})


@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    try:
        data = request.get_json(force=True)
        operation = data.get('operation')
        a = data.get('a')
        b = data.get('b')

        if operation is None:
            return jsonify({'error': 'Operation is required'}), 400
        if a is None:
            return jsonify({'error': 'Operand a is required'}), 400

        a = float(a)
        if operation not in ['sqrt']:
            if b is None:
                return jsonify({'error': 'Operand b is required for this operation'}), 400
            b = float(b)

        result = calculate(operation, a, b)
        return jsonify({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        })
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:
        return jsonify({'error': f'Unexpected server error: {str(exc)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
