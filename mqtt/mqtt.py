import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time
from datetime import datetime

class MQTT:
    # Pi:
    # alias = "Pi"
    # server = "localhost"
    # path_publish = "pi_channel"
    # path_subscribe = "laptop_channel"
    def __init__(self, alias, server, path_publish, path_subscribe):
        #MQTT Broker address
        self.alias = alias
        self.MQTT_SERVER = server  # Replace with the actual IP address of the Raspberry Pi
        self.MQTT_PATH_PUBLISH = path_publish
        self.MQTT_PATH_SUBSCRIBE = path_subscribe

        self.message = ""

        #Setup MQTT client
        mqtt_client = mqtt.Client()
        mqtt_client.on_connect = self.on_connect
        mqtt_client.on_message = self.on_message
        mqtt_client.connect(self.MQTT_SERVER, 1883, 60)

        #Start the MQTT client
        mqtt_client.loop_start()

    #The callback for when the client receives a CONNACK response from the server
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(self.MQTT_PATH_SUBSCRIBE)

    #The callback for when a PUBLISH message is received from the server
    def on_message(self, client, userdata, msg):
        self.message = str(msg.payload.decode())
        # print(msg.topic + " - " + str(msg.payload.decode()))

    def publish(self, message):
        jmsg = json.dumps(message, indent=4)
        publish.single(self.MQTT_PATH_PUBLISH, jmsg, hostname=self.MQTT_SERVER)
        # print(f"Published from {self.alias}: {jmsg}")

if __name__ == '__main__':
    # To test the script, run the the bellow code once and another time commented out
    mqtt = MQTT("Pi", "localhost", "pi_channel", "laptop_channel")
    while True:
        dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        message = {
            "temperature": "23.0",
            "timestamp": dt,
            "light": "on"
        }
        mqtt.publish(message)
        time.sleep(5)

    mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
    while True:
        dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        message = {
            "type-id": "de.uni-stuttgart.iaas.sc.laptop",
            "instance-id": "laptop instance",
            "timestamp": dt,
            "value": {
                "temperature": "23.0"
            }
        }
        mqtt.publish(message)
        time.sleep(5)