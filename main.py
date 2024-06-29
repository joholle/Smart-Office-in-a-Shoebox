import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time
from datetime import datetime
from arduinoSerial import ArduinoSerial

#MQTT Broker address
MQTT_SERVER = "localhost"  # Replace with the actual IP address of the Raspberry Pi
MQTT_PATH_PUBLISH = "pi_channel"
MQTT_PATH_SUBSCRIBE = "laptop_channel"

#The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH_SUBSCRIBE)

#The callback for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode()))

#Setup MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_SERVER, 1883, 60)

#Start the MQTT client
mqtt_client.loop_start()

#Start Serial port connection to arduino
arduinoSerial = ArduinoSerial()

#Publish messages in a loop
while True:
    dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
    message = arduinoSerial.read()
    jmsg = json.dumps(message, indent=4)
    publish.single(MQTT_PATH_PUBLISH, jmsg, hostname=MQTT_SERVER)
    print(f"Published from Pi: {jmsg}")
    time.sleep(5)