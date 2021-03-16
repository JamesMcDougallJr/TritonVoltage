sudo apt-get install libusb-dev -y
git clone https://github.com/PaulStoffregen/teensy_loader_cli.git teensy_loader
cd teensy_loader && make
cp ./donkey/* ~/projects/d3/
