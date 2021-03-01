import os, pty
from serial import Serial
import threading

def test_serial():
    """Start the testing"""
    master,slave = pty.openpty() #open the pseudoterminal
    s_name = os.ttyname(slave) #translate the slave fd to a filename

    #open a pySerial connection to the slave
    print(s_name)
    with Serial(s_name, 9600, timeout=0) as ser:
        print('Serial Port opened')
        while True:
            ser.write(b'4.12,5.78,11.12\n') #write the first command

if __name__=='__main__':
    test_serial()
