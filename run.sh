cd server && python3 -m flask run &> /dev/null &
sleep 2
visdom -port 5001 &
sleep 2
python3 client/visdom_publisher.py &> /dev/null &
