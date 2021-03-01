import serial
import time
import sys
DEFAULT_PORT="/dev/ttyACM0"
def reading(port=DEFAULT_PORT):
    with serial.Serial(port) as ser:
        line = []
        while True:
            try:
                char = ser.read(1).decode()
                print('char: {}'.format(char))
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
        print('Voltage Reading: {}'.format(reading(DEFAULT_PORT)))
    else:
        print('Voltage Reading: {}'.format(reading(sys.argv[0])))
