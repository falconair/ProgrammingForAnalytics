#serve text
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get('/status')
def status():
    return "OK"


@app.get('/get_time')
def get_time():
    t = f'current time is {datetime.now().strftime("%H:%M")}'
    return t

# fastapi dev serve_text.py