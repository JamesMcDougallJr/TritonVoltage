#!/usr/bin/env python
import Jetson.GPIO as GPIO
import time
import sys

# Pin Definitions
output_pin = 12  # BCM pin 18, BOARD pin 12

def main(timeout):
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            GPIO.output(output_pin, GPIO.LOW)
            print('Sleep {} seconds.'.format(timeout))
            time.sleep(timeout)
            print('Awakening.')
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(0.1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(15)
