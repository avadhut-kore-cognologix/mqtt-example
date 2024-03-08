sudo apt-get update
sudo apt-get -y install micropython
micropython -m upip install umqtt.simple
micropython -m upip install random

micropython xpanse-micropython/mca.py
micropython xpanse-micropython/hca.py