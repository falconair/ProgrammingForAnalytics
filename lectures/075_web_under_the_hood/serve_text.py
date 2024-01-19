#serve text
from datetime import datetime
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.get('/status')
def status():
    return "OK"

@app.get('/get_time')
def get_time():
    t = f'current time is {datetime.now().strftime("%H:%M")}'
    return t

if __name__=='__main__': 
    app.run(debug=True, port=5000) #host='0.0.0.0' <= Listen to all traffic, not just local