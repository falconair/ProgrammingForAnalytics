#serve post json
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

@app.get('/status')
def status():
    d = {'status': 'OK'}
    return jsonify(d)

@app.get('/get_time')
def get_time():
    d = {'current_time':datetime.now().strftime("%H:%M")}
    return jsonify(d)

@app.post('/get_churn_probability')
def get_churn_probability():

    client_properties = request.get_json()
    print(client_properties)
    print(type(client_properties))

    #if 'UC_GRAD' not in client_properties:
    #    pass throw error

    # Our churn model is fake, we don't actually use an ML model :(
    if client_properties['uc_grad']:
        return jsonify({'churn_prob':0.34})
    else:
        return jsonify({'churn_prob':0.87})

if __name__=='__main__': 
    app.run(debug=True, port=5000) #host='0.0.0.0' <= Listen to all traffic, not just local