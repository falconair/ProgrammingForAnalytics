#serve json
from datetime import datetime
import requests

HOST = 'localhost'
PORT = 5000

# Request something which doesn't exist
response = requests.get(url=f'http://{HOST}:{PORT}/')
print(f"Result of doing a GET request from http://{HOST}:{PORT}/")
print(response)

print("-------------")

# Request the time
response = requests.get(url=f'http://{HOST}:{PORT}/get_time')
print(f"Result of doing a GET request from http://{HOST}:{PORT}/get_time")
print(response)
print("Response raw content:" + dir(response))

if __name__=='__main__': 
    pass