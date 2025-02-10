#serve json
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get('/status')
def status():
    d = {'status': 'OK'}
    return d

@app.get('/get_time')
def get_time():
    d = {'current_time':datetime.now().strftime("%H:%M")}
    return d

# fastapi dev serve_json.py