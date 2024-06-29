import time
from datetime import datetime
import json
import paho.mqtt.client as mqtt

class Simulator:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        mqtt_publisher = mqtt.Client(client_id='TemperaturePublisher')
        mqtt_publisher.connect('127.0.0.1', 1883, 60)
        mqtt_publisher.loop_start()
        
        while True:
            dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
            message = {
                "type-id": "de.uni-stuttgart.iaas.sc." + "test type",
                "instance-id": "test instance",
                "timestamp": dt,
                "value": {
                    "test unit": "test value"
                }
            }

            jmsg = json.dumps(message, indent=4)
            mqtt_publisher.publish('u38/0/353/window/' + "test type" + '/' + "test instance", jmsg, qos=2)
            print(f"Published: {jmsg}")
            time.sleep(self.interval)

s = Simulator(5)
s.start()
