import datetime, time, json
from mqtt.mqtt import MQTT
from arduinoSerial import ArduinoSerial


class Pi:
    def __init__(self):
        self.mqtt = MQTT("Pi", "localhost", "pi_channel", "laptop_channel")
        self.arduinoSerial = ArduinoSerial()
        self.old_messages = []

    def loop(self):
        dt = datetime.datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        sensor_readings = self.arduinoSerial.read()
        if sensor_readings != "":
            sensor_readings["timestamp"] = dt
            self.mqtt.publish(sensor_readings)

        self.wait_for_callback()

    def wait_for_callback(self):
        timer = time.time()
        while timer + 2 > time.time():
            if self.mqtt.on_message:
                recieved_message = self.mqtt.message
                if recieved_message != "" and recieved_message not in self.old_messages:
                    self.old_messages.append(recieved_message)
                    self.act_on_recieved_message(recieved_message)

    def act_on_recieved_message(self, message):
        dt = datetime.datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        if "set initial state" in message:
            print(str(dt) + ": setting initial state")
            self.arduinoSerial.write("servo 0")
            self.arduinoSerial.write("lights off")
            self.arduinoSerial.write("fan off")
            self.arduinoSerial.write("cooler off")
        if "open window" in message:
            print(str(dt) + ": opening window")
            self.arduinoSerial.write("servo 180")
        elif "close window" in message:
            print(str(dt) + ": closing window")
            self.arduinoSerial.write("servo 0")
        elif "turn on lights" in message:
            print(str(dt) + ": turning on lights")
            self.arduinoSerial.write("lights on")
        elif "turn off lights" in message:
            print(str(dt) + ": turning off lights")
            self.arduinoSerial.write("lights off")
        elif "turn on airconditioner" in message:
            print(str(dt) + ": turning on AC")
            self.arduinoSerial.write("fan on")
            self.arduinoSerial.write("cooler on")
        elif "turn off airconditioner" in message:
            print(str(dt) + ": turning off AC")
            self.arduinoSerial.write("fan off")
            self.arduinoSerial.write("cooler off")
        else:
            print(str(dt) + "unknown instruction: " + str(message.strip()))
                    
                


if __name__ == '__main__':
    pi = Pi()
    while True:
        pi.loop()