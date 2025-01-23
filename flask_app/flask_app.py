# Create a basic Flask app to handle backend processing
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    inputs = data.get('inputs', [])
    try:
        result = sum(inputs)  # Example calculation: sum of inputs
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Save the Flask app code to a file
flask_code = '''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    inputs = data.get('inputs', [])
    try:
        result = sum(inputs)  # Example calculation: sum of inputs
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''

with open('/root/flask_app.py', 'w') as f:
    f.write(flask_code)
