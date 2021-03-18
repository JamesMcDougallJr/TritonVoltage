# ECE/MAE 148 Battery Monitor
 
This is an Arduino script for the final project of the course ECE 148 - Intro to Autonomous Vehicles.

Functionality:
1) Three ADC Channels (A9, A3, A6) on the Teensy board are used to read the LIPO battery's voltages. These channels are configurable and can be changes as per needed. 
2) Teensy reads the ADC channels when it receives a rising edge interrupt on pin-2.
3) We take average of 512 ADC readings on each channel. Each ADC read is spaced with a 2 MSec delay.
4) When all the 3 ADC channel are read, we compute the corresponding voltages for 4V, 8V, 12V create a character string and send the message over the USB.

Test mode: 
1) When test mode is toggled on, the Teensy Pin-6 generate a rising edge signal.
2) This signal can be used to wake up the Teensy by the interrupt on Pin-2.
3) Test mode also comes with some logging messages.


