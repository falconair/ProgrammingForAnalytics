#serve post json
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/status')
def status():
    d = {'status': 'OK'}
    return d

@app.get('/get_time')
def get_time():
    d = {'current_time':datetime.now().strftime("%H:%M")}
    return d

class ClientData(BaseModel):
    gender: str
    age: int
    uc_grad: bool

@app.post('/get_churn_probability')
def get_churn_probability(client_props: ClientData):

    #if 'UC_GRAD' not in client_properties:
    #    pass throw error

    # Our churn model is fake, we don't actually use an ML model :(
    if client_props.uc_grad == "true":
        return {'churn_prob':0.34}
    else:
        return {'churn_prob':0.87}

# fastapi dev serve_post_json.py