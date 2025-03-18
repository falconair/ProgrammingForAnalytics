
from fastapi import FastAPI
from typing import Dict
from ray import serve
import ray

#ray.init(address="192.168.12.239:10001") 
#ray.init(ignore_reinit_error=True)

app = FastAPI()

@app.get("/status")
def status() -> Dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.get("/compute")
def fibonacci(n: int):
    """Compute Fibonacci sequence up to n (inclusive)."""
    if n <= 0:
        return []
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

@serve.deployment
@serve.ingress(app)
class FastAPIWrapper:
    pass

serve.run(FastAPIWrapper.bind(), route_prefix="/")

# python simple_api_ray.py
# http://localhost:8000/compute?n=10
