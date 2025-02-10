#serve post json
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get('/status')
def status():
    d = {'status': 'OK'}
    return d

@app.get('/get_time_old')
def get_time():
    d = {'current_time':datetime.now().strftime("%H:%M")}
    return d

@app.post('/get_churn_probability_old')
def get_churn_probability_old():

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

@app.post('/get_churn_probability')
def get_churn_probability(uc_grad):

    #if 'UC_GRAD' not in client_properties:
    #    pass throw error

    # Our churn model is fake, we don't actually use an ML model :(
    if uc_grad == "true":
        return {'churn_prob':0.34}
    else:
        return {'churn_prob':0.87}

# fastapi dev serve_post_json.py