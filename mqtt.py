import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    print('Message topic: {}'.format(message.topic))
    print('Message payload:')
    print(json.loads(message.payload.decode()))

def on_connect(client, userdata, flags, rc):
    print("Connected! Result code: " + str(rc))
    client.subscribe('u38/0/353/window/+/+', qos=2)

mqtt_subscriber = mqtt.Client(client_id='TemperatureSubscriber')
mqtt_subscriber.on_message = on_message
mqtt_subscriber.on_connect = on_connect

mqtt_subscriber.connect('127.0.0.1', 1883, 60)
mqtt_subscriber.loop_forever()
