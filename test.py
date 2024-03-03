from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, Gavin!'})

if __name__ == 'test':

    app.run(debug=True)
