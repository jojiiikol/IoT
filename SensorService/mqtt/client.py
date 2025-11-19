from paho.mqtt.client import Client, CallbackAPIVersion

from config import MqttConfig


class MqttClient:
    def __init__(self, mqtt_config: MqttConfig = MqttConfig()):
        self.config = mqtt_config
        self.client = Client(CallbackAPIVersion.VERSION2)
        self.client.on_message = self.handler

    def connect(self):
        self.client.connect(self.config.host, self.config.port, 60)

    def subscribe(self, topic: str):
        self.client.subscribe(topic)

    def handler(self, client, userdata, message):
        print(message.topic, message.payload.decode())

    def start(self):
        self.client.loop_start()


