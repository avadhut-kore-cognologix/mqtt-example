sudo apt-get update
sudo apt-get -y install micropython
micropython -m upip install umqtt.simple

micropython tcp/sub.py
micropython tcp/pub.py