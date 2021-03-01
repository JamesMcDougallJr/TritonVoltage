from flask import Flask
from .voltage import voltage_subscriber as subscriber

app = Flask(__name__)

@app.route('/')
def root():
    return subscriber.reading()
