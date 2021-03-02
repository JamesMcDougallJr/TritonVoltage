import serial
import time
import sys

class BatteryMonitor(object):

    self.timeout = 10
    self.last_check_time = time.time()

    def __init__(self, port="/dev/ttyACM0", cutoff=3):
        self.port = port
        self.cutoff = cutoff

    """
        When in Donkey, this function is executed every few iterations.
    """
    def run(self):
        if time.time() - self.timeout > self.last_check_time:
            voltages, danger = adjusted_voltages()
            if danger:
                print('One of the cells is dangerously low!')
            print('Cell 0: {}\tCell 1: {}\tCell 2: {}'.format(voltages[0], voltages[1], voltages[2]))
            self.last_check_time = time.time()


    """
        Adjusted Voltages are the voltages obtained by subtracting the highest from the second highest,
        and the second highest from the first highest
    """
    def adjusted_voltages(self):
        try:
            voltages = [round(float(v), 2) for v in self.reading().split(',')]
        except:
            # probably the reading was incorrect
            return []
        danger_readings = [voltage < self.cutoff for voltage in voltages]
        danger = True in danger_readings:
        return [voltages[0],voltages[1] - voltages[0],voltages[2] - voltages[1]], danger


    """
        Just the straight serial reading, as a string
    """
    def reading(self):
        with serial.Serial(self.port) as ser:
            line = []
            while True:
                try:
                    char = ser.read(1).decode()
                    # messages will be surrounded by \nX,X,X\n
                    if char == '\n':
                        # then read in the next few bytes until the next newline.
                        voltages = ser.readline().decode().strip()
                        return voltages
                except:
                    return ''

if __name__ == '__main__':
    if len(sys.argv) > 0:
        battmon = BatteryMonitor()
    else:
        battmon = BatteryMonitor(sys.argv[1])
    print('Voltage Reading: {}'.format(battmon.adjusted_voltages())
