from visdom import Visdom
import requests
import numpy as np
import time

viz = Visdom(port=5001)
plot = viz.line(
    X = np.array([1, 1]),
    Y = np.array([12, 12]),
    env='main'
)

i = 1
while True:
    r = requests.get('http://127.0.0.1:5000')
    voltages = [int(v) for v in r.text.split(',')]
    viz.line(X=np.array([i]), Y=np.array([voltages[0]]), env='main', win=plot, name='Triton Voltage', update = 'replace', opts=dict(fillarea=True))
    time.sleep(2)
    i += 1
