from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    try:
        if num1 is None:
            return jsonify({'error': 'num1 is required'}), 400

        num1 = float(num1)
        num2 = float(num2) if num2 is not None else None

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))
        elif operation == 'sqrt':
            if num1 < 0:
                return jsonify({'error': 'Square root is not defined for negative numbers'}), 400
            result = math.sqrt(num1)
        elif operation == 'square':
            result = num1 ** 2
        elif operation == 'cube':
            result = num1 ** 3
        else:
            return jsonify({'error': 'Unsupported operation'}), 400

        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid numeric input'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
