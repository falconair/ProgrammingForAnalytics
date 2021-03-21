from flask import Flask, request
from joblib import load

import numpy as np
import pandas as pd

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

    pclass, age, sibsp, parch, fare, adult_male, alone = float(args.get('pclass')), float(args.get('age')), float(args.get('sibsp')), float(args.get('parch')), float(args.get('fare')), float(args.get('adult_male')), float(args.get('alone'))

    print(pclass, age, sibsp, parch, fare, adult_male, alone)
    
    input_array = np.array([[pclass, age, sibsp, parch, fare, adult_male, alone]])
    
    print(input_array)
    
    predicted = trained_model.predict(input_array)
    return args, predicted

if __name__ == "__main__":
    app.run()  
    
# Test as:
# http://localhost:5000/model?pclass=1&age=15&sibsp=0&parch=1&fare=211.3375&adult_male=0&alone=0
# 1.    ,  15.    ,   0.    ,   1.    , 211.3375,   0.    ,0.