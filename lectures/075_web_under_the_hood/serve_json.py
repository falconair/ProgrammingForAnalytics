#serve json
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

if __name__=='__main__': 
    app.run(debug=True, port=5000) #host='0.0.0.0' <= Listen to all traffic, not just local