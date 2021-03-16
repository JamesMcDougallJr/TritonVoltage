# Triton Voltage

Triton Voltage starts a flask server that reads serial data from an arduino representing the voltages of three cells in a lithium ion battery.

To build the circuit, you need the following materials:

    1. One Lithium Ion Battery, with 4 pins - three voltage pins, 1 ground. Currently the circuit is designed for a 12v LIPO.
    3. One Jetson Nano
    4. One Teensy v3.2
    5. Male to Female and Female to Female Wires
    6. Wire Cutters
    7. One PCB design board (or a breadboard if you have no other options)
   
Looking at the battery, do the following:
    1. Use a multimeter, put the ground into the black wire on the LiPo testing port.
    2. Put the red wire into each of the ports for a few seconds so you can see the voltages.
    3. It goes, from closest to the ground port to the furthest, (~4V -> ~8V -> ~12V)

To build the circuit, do the following:
    1. Look at the diagram below to get an idea of what resistors you will need.
    2. Solder the resistors in series according to the diagram.
    3. Solder a ground wire connecting all three channels - they all should have the same ground
    4. Solder male jumper wires to the end of the PCB (3 red ones). These will go into the battery so make sure they can fit.
    5. Solder female jumper wires to the end of the PCB (3 yellow ones). These will connect to the teensy ADC pins.
    6. Hot glue the jumper wires so they don't break off.
    7. Connect the jumper wires to the battery and test voltages using a multimeter. 
    8. Mark the channels with a marker or a label so you know which channel goes to which part of the battery.

Install Required Software
    1. Look at install.s. This should work but assumes some paths.
    2. Change the path ~/projects/d3/ to your own donkey d3 or d3_sim path.
    3. Run ``pip install -r requirements.txt``

Setup Your Environment
    1. Be sure to ssh in with tunneling so you can view the visdom server
        `ssh -L 5000:localhost:5000 -L 5001:localhost:5001 jetson@ucsdrobocar-148-0X`

Run the program - run.sh
    1. Execute run.sh
    2. Attempts to start the clock on GPIO 12 with a 2s sleep.
    3. Then it loads the teensy with the required .hex file -> generated from the .ino file.
    4. Press the reset button on the Teensy when prompted.
    5. Then the flask server starts to serve the voltage. You can also visit it in the browser at port 5000 if you tunnel in.
    6. Start the visdom server. You must be tunneled in for this to work. `visdom -port 5001` or `python3 -m visdom.server -port 5001`
    7. Start the visdom publisher, which grabs data from the voltage server and publishes it to the visdom server in the right format. `python3 client/visdom_client.py`
