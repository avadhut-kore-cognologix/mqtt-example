# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client

from sensordata import generate_sensor_data

from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("xpanse-python3/config.ini")
mqtt_config = config_object["MQTTCONFIG"]


# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(mqtt_config["username"], mqtt_config["password"])
    client.on_connect = on_connect
    client.connect(mqtt_config["broker"], int(mqtt_config["port"]))
    return client


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        topic = "python/mqtt"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        # if msg_count > 5:
        #     break

def randomPublish(client, topics):
    msg_count = 1
    while True:
        time.sleep(1)
        topic = random.choice(topics)
        msg = str(generate_sensor_data())
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        # if msg_count > 5:
        #     break


def run():
    client = connect_mqtt()
    client.loop_start()
    topics = config_object.get("MQTTCONFIG", "topics").split("\n")
    # publish(client)
    randomPublish(client, topics)
    client.loop_stop()


if __name__ == '__main__':
    run()
