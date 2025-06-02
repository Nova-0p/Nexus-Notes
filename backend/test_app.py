from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Flask backend is working!', 'status': 'success'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Backend is running'})

@app.route('/test')
def test():
    return jsonify({'message': 'Test route is working!'})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)