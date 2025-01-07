
import os
import sys

if len(sys.argv) < 2:
    print("Error: Missing enviornment variable name. Please run as 'python program5.py <ENV>`")
    sys.exit(1)
    
ENV = sys.argv[1]
ENV_VAL = os.environ.get(ENV, "")

print(f"Environment variable {ENV} has value {ENV_VAL}")
