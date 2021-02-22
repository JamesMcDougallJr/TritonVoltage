import serial
import time
PORT="/dev/ttyACM0"
def reading():
    with serial.Serial(PORT) as ser:
        line = []
        while True:
            try:
                char = ser.read(1).decode()
                # messages will be surrounded by \nX,X,X\n
                # if I see a char and there is stuff in the buffer, and that stuff is good, return it.
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
        if char != ',':
            current += char
        else:
            nums.append(int(current))
    return nums

if __name__ == '__main__':
    print('Voltage Reading: {}'.format(reading()))
