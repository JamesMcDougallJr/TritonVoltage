from visdom import Visdom
import requests
import numpy as np
import time

viz = Visdom(port=5001)
plot = viz.line(
    X = np.array([1, 1]),
    Y = np.array([0, 0]),
    env='main',
    opts=dict(
        legend=['Cell 1 Voltage', 'Cell 2 Voltage', 'Cell 3 Voltage'],
        title='Triton Voltages'
    )
)

i = 1
while True:
    r = requests.get('http://127.0.0.1:5000')
    voltages = [float(v) for v in r.text.split(',')]
    print(voltages)
    voltages[2] = voltages[2] - voltages[1]
    voltages[1] = voltages[1] - voltages[0]
    print(voltages)
    for j in range(3):
        viz.line(X=np.array([i]), Y=np.array([voltages[j]]), env='main', win=plot, name='Cell {} Voltage'.format(j), update = 'append')
    time.sleep(2)
    i += 1
