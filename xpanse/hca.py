# hca.py
# Hardware Connector Application
import time
import random
from umqtt.simple import MQTTClient

SERVER="localhost"
ClientID = f'raspberry-hca-sub-{time.time_ns()}'
user = "mqttuser"
password = "mqtt"
topicsToSubscribe = ["xpanse/sensordata/request"]
client = MQTTClient(ClientID, SERVER, 1883, user, password)

def generate_sensor_data():
    # round(random.uniform(0.0,20.0), 2)
    sensor_data = {
        "timestamp": int(time.time()),
        "device_id":"dev123",
        "sensor_id":"sensor123",
        "data":{"windspeed": 5.9}
    }
    return sensor_data

def publishMessage(topic, msg):
    print('send message %s on topic %s' % (msg, topic))
    client.publish(topic, msg, qos=0)

def sub(topic, msg):
    print('received message %s on topic %s' % (msg, topic))
    responseTopic = 'xpanse/sensordata/response'
    responseMsg = str(generate_sensor_data())
    publishMessage(responseTopic, responseMsg)

def main(server=SERVER):
    client.set_callback(sub)
    client.connect()
    print('Connected to MQTT Broker "%s"' % (server))

    for topic in topicsToSubscribe:
        client.subscribe(topic)
    while True:
        if True:
            client.wait_msg()
        else:
            client.check_msg()
            time.sleep(5)

if __name__ == "__main__":
    main()
