## Install dependencies
sudo apt-get install mosquitto mosquitto-clients
pip3 install "paho-mqtt<2.0.0"


## start the subscriber
python3 xpanse-python3/sub.py


## start the published
python3 xpanse-python3/pub.py
