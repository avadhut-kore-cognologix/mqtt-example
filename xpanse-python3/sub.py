# python3.6

from configparser import ConfigParser
import random

from paho.mqtt import client as mqtt_client

config_object = ConfigParser()
config_object.read("xpanse-python3/config.ini")
mqtt_config = config_object["MQTTCONFIG"]

# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected MQTT disconnection. Will auto-reconnect")

    client = mqtt_client.Client(client_id, clean_session=False)
    client.username_pw_set(mqtt_config["username"], mqtt_config["password"])
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(mqtt_config["broker"], int(mqtt_config["port"]))
    return client


def subscribe(client: mqtt_client, topics):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    for topic in topics:
        client.subscribe(topic, qos=2)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    topicsToSubscribe = config_object.get("MQTTCONFIG", "topics").split("\n")
    subscribe(client, topicsToSubscribe)
    client.loop_forever()


if __name__ == '__main__':
    run()
