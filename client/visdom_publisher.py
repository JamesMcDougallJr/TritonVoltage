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
        legend       = ['Cell Voltage (4V)', 'Cell Voltage (8V)', 'Cell Voltage(12V)'],
        title        = 'Triton Voltages (LIPO Battery)',
        xlabel       = 'Time (seconds)',
        ylabel       = 'Voltage (V)',
        marginleft   = 30,
        marginright  = 30,
        marginbottom = 80,
        margintop    = 30,
        showgrid     = True
    )
)

normalized_plot = viz.line(
    X = np.array([1, 1]),
    Y = np.array([0, 0]),
    env='main',
    opts=dict(
        legend       = ['Cell 0 Voltage', 'Cell 1 Voltage', 'Cell 2 Voltage'],
        title        = 'Triton Voltages (LIPO Battery) - Normalized',
        xlabel       = 'Time (seconds)',
        ylabel       = 'Voltage (V)',
        marginleft   = 30,
        marginright  = 30,
        marginbottom = 80,
        margintop    = 30,
        showgrid     = True
    )
)

print('Hello')
i = 1
while True:
    r = requests.get('http://127.0.0.1:5000')
    print(r.text)
    voltages = [float(v) for v in r.text.split(',')]
    normalized_voltages = [None]*3
    normalized_voltages[0] = voltages[0]
    normalized_voltages[1] =  voltages[1] - voltages[0]
    normalized_voltages[2] = voltages[2] - voltages[1]
    print(voltages)
    for j,v in zip(range(3), ['4', '8', '12']):
        viz.line(X=np.array([i]), Y=np.array([voltages[j]]), env='main', win=plot, name='Cell Voltage ({}V)'.format(v), update = 'append')
        viz.line(X=np.array([i]), Y=np.array([normalized_voltages[j]]), env='main', win=normalized_plot, name='Cell {} Voltage'.format(j), update = 'append')
    time.sleep(2)
    i += 1
