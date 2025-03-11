
import ray
from ray import serve
from fastapi import FastAPI

ray.init(address="auto")  # Connect to the existing Ray cluster

serve.start(detached=True)  # Ensure Serve runs in the background

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Ray Serve"}

# Create a deployment with multiple replicas
@serve.deployment(num_replicas=2)
@serve.ingress(app)
class FastAPIDeployment:
    pass

FastAPIDeployment.deploy()

print("FastAPI app is deployed. Try accessing it at the head node's IP.")
