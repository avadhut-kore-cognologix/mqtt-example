sudo apt-get update
sudo apt-get -y install micropython
micropython -m upip install umqtt.simple
micropython -m upip install random

micropython tcp/sub.py
micropython tcp/pub.py

micropython xpanse/mca.py
micropython xpanse/hca.py