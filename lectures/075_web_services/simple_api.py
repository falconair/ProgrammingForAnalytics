
from fastapi import FastAPI
from typing import Dict

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

# fastapi run simple_api.py
# http://localhost:8000/compute?n=10
