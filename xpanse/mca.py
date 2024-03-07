# mca.py
# Mobile Connector Application
import time
from umqtt.simple import MQTTClient

server="localhost"
ClientID = f'raspberry-mca-pub-{time.time_ns()}'
user = "mqttuser"
password = "mqtt"
topicsToSubscribe = ["xpanse/sensordata/response"]

def sub(topic, msg):
    print('received message %s on topic %s' % (msg, topic))

def connect():
    print('Connected to MQTT Broker "%s"' % (server))
    client = MQTTClient(ClientID, server, 1883, user, password)
    client.set_callback(sub)
    client.connect()
    for topic in topicsToSubscribe:
        client.subscribe(topic)
    return client

def reconnect():
    print('Failed to connect to MQTT broker, Reconnecting..."%s"' % (server))
    time.sleep(5)
    client.reconnect()

def publishMessage(topic, msg):
    print('send message %s on topic %s' % (msg, topic))
    client.publish(topic, msg, qos=0)


try:
    client = connect()
except OSError as e:
    reconnect()

while True:
  requestTopic = 'xpanse/sensordata/request'
  requestMsg = b'{"request":"sensordata","datapoint":"windspeed","device_id":"dev123","sensor_id":"sensor123"}'
  publishMessage(requestTopic, requestMsg)
  client.wait_msg()
  time.sleep(5)
