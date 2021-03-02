
echo "Starting Clock at 2s"
python3 ~/TritonVoltage/server/voltage/clock.py 2 &> /dev/null &

echo "Flashing Teensy"
#https://github.com/PaulStoffregen/teensy_loader_cli
./teensy_loader/teensy_loader_cli --mcu=mk20dx256 -w ./Teensy/teensy-test.ino.TEENSY32.hex -v # only for teensy 3.2
sleep 2
echo "Start Flask Server to publish voltages"
cd server && python3 -m flask run &> /dev/null &
sleep 2
echo "Start vidom server to host plots"
visdom -port 5001 &
sleep 2
echo "Start visdom publisher to publish data to plots."
python3 client/visdom_publisher.py &> /dev/null &
