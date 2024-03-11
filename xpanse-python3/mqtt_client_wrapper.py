from paho.mqtt import client as MQTTClient
import time

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

class MQTTClientWrapper:
    def __init__(self, server, port, clientId, username, password):
        self.server = server
        self.clientId = clientId
        self.username = username
        self.password = password
        self.port = port

        self.client = MQTTClient.Client(self.clientId)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect

    def connect(self):
        print(self.clientId, 'Connected to MQTT Broker "%s"' % (self.server))
        self.client.connect(self.server, self.port)
    

    def reconnect(self):
        print(self.clientId, 'Failed to connect to MQTT broker, Reconnecting..."%s"' % (self.server))
        time.sleep(5)
        self.client.reconnect()

    def publishMessage(self, topic, message):
        self.client.loop_start()
        result = self.client.publish(topic, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        self.client.loop_stop()

    def setCallback(self, callback):
        self.client.on_message = callback

    def subscribeToTopics(self, topics):
        for topic in topics:
            self.client.subscribe(topic)

    def waitForMessage(self):
        self.client.loop_forever()