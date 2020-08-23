from flask import Flask, request

from joblib import load

# Load trained model
trained_model = load('model.joblib')


# Flask server setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/model')
def serve_model():
    args = request.args
    print(args)
    print(args.get('pclass'))
    return args