from flask import Flask
from .voltage import voltage

app = Flask(__name__)

@app.route('/')
def root():
    return voltage.reading()

