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

