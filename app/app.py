import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"Hello World! I am {hostname}"