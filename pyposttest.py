import sys
import tracemalloc
import requests
import json

tracemalloc.start()

data = {
    "name": "lovergirl",
}
def quickpost(data):
    r = requests.post("http://127.0.0.1:8000/new_name", json.dumps(data))
    print(r.status_code)
    

quickpost(data)