from umqtt.simple import MQTTClient
import time

class MQTTClientWrapper:
    def __init__(self, server, clientId, username, password):
        self.server = server
        self.clientId = clientId
        self.username = username
        self.password = password
        self.client = MQTTClient(self.clientId, self.server, 1883, self.username, self.password)

    def connect(self):
        print(self.clientId, 'Connected to MQTT Broker "%s"' % (self.server))
        self.client.connect()

    def reconnect(self):
        print(self.clientId, 'Failed to connect to MQTT broker, Reconnecting..."%s"' % (self.server))
        time.sleep(5)
        self.client.reconnect()

    def publishMessage(self, topic, message):
        self.client.publish(topic, message, qos=0)

    def setCallback(self, callback):
        self.client.set_callback(callback)

    def subscribeToTopics(self, topics):
        for topic in topics:
            self.client.subscribe(topic)

    def waitForMessage(self):
        self.client.wait_msg()

    def CheckMessage(self):
        self.client.check_msg()