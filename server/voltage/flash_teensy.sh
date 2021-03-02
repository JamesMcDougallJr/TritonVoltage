echo "Flashing Teensy"
teensy_loader_cli --mcu=mk20dx256 -w ~/Arduino/ECE-MAE-148-Battery-Monitor/teensy-test/teensy-test.ino.TEENSY32.hex -v
