# mca.py
# Mobile Connector Application
import time
from mqtt_client_wrapper import MQTTClientWrapper


def main():
    server="localhost"
    clientId = f'raspberry-mca-pub-{time.time_ns()}'
    username = "mqttuser"
    password = "mqtt"
    topicsToSubscribe = ["xpanse/sensordata/response"]
    client = MQTTClientWrapper(server, clientId, username, password)

    try:
        client.setCallback(sub)
        client.connect()
        client.subscribeToTopics(topicsToSubscribe)
    except OSError as e:
        client.reconnect()

    while True:
        requestTopic = 'xpanse/sensordata/request'
        requestMsg = b'{"request":"sensordata","datapoint":"windspeed","device_id":"dev123","sensor_id":"sensor123"}'
        client.publishMessage(requestTopic, requestMsg)
        client.waitForMessage()
        time.sleep(5)

def sub(topic, msg):
    print('-------------------------------------------------------------------')
    print('received message %s on topic %s' % (msg, topic))

main()