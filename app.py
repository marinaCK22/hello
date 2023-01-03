import requests as requests
from flask import Flask

app = Flask(__name__)
BASE_URL = "127.0.0.1"
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/algo")
def hello_world_from_algo():
    response = requests.get(f"http://{BASE_URL}:5001/")
    res = str(response.text)
    return res

@app.route("/algo_1")
def hello_world_from_algo1():
    response = requests.get(f"http://18.117.98.137:5000/")
    res = str(response.text)
    return res

@app.route("/algo_2")
def hello_world_from_algo2():
    response = requests.get(f"http://10.200.0.253:5000/")
    res = str(response.text)
    return res
