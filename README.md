# Triton Voltage

Triton Voltage starts a flask server that reads serial data from an arduino representing the voltages of three cells in a lithium ion battery.

To build the circuit, you need the following materials:
    1. One Lithium Ion Battery, with 4 pins - three voltage pins, 1 ground. Currently the circuit is designed for a 12v LIPO.
    2. One Jetson Nano
    3. One Teensy v3.2
    4. Male to Female and Female to Female Wires
    5. Wire Cutters

Install Required Software
    1. Look at install.s. This should work but assumes some paths.
    2. Change the path ~/projects/d3/ to your own donkey d3 or d3_sim path.
    3. Run ``pip install -r requirements.txt``

Setup Your Environment
    1. Be sure to ssh in with tunneling so you can view the visdom server
        `ssh -L 5000:localhost:5000 -L 5001:localhost:5001 jetson@ucsdrobocar-148-0X`

Run the program
    1. Execute run.sh
    2. This script attempts to start the clock on GPIO 12 with a 2s sleep.
    3. Then it loads the teensy with the required .hex file -> generated from the .ino file.
    4. Press the reset button on the Teensy when prompted.
    5. Then the flask server starts to serve the voltage. You can also visit it in the browser at port 5000 if you tunnel in.
    6. Start the visdom server. You must be tunneled in for this to work.
    7. Start the visdom publisher, which grabs data from the voltage server and publishes it to the visdom server in the right format.

Donkeycar Setup
    1. In the serv
