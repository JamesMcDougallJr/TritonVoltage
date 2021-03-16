from flask import Flask
from .voltage import BatteryMonitor as bm

app = Flask(__name__)
battmon = bm.BatteryMonitor()

@app.route('/')
def root():
    reading, danger = battmon.reading() if battmon.available() else battmon.simulated_voltages()
    print(reading)
    return ','.join([str(volt) for volt in reading])
