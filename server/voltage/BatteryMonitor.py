import serial
import time
import sys
class BatteryMonitor(object):
    def __init__(self, port="/dev/ttyACM0", cutoff=3):
        self.port = port
        self.cutoff = cutoff

    def run(self):
        voltages = adjusted_voltages()
        print('Cell 0: {}\tCell 1: {}\tCell 2: {}'.format(voltages[0], voltages[1], voltages[2]))

    def adjusted_voltages(self):
        voltages = [round(float(v), 2) for v in self.reading().split(',')
        return [voltages[0],voltages[1] - voltages[0],voltages[2] - voltages[1]]


    def reading(port=DEFAULT_PORT):
        with serial.Serial(port) as ser:
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

    def condense(line):
        if len(line) <= 0:
            return []
        nums = []
        current = ''
        for char in line:
            if char != ',' and char != '\n':
                current += char
            else:
                nums.append(float(current))
                current = ''
        if current != '':
            nums.append(float(current, ))
        return nums

if __name__ == '__main__':
    if len(sys.argv) > 0:
        battmon = BatteryMonitor()
    else:
        battmon = BatteryMonitor(sys.argv[1])
    print('Voltage Reading: {}'.format(battmon.adjusted_voltages())
