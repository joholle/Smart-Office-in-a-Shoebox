import serial, json, time

class ArduinoSerial:
    def __init__(self):
        # listen and send commands to arduino serial port 9600
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)

    def read(self):
        reading = ""
        self.ser.write(b"read\n")
        for line in self.ser.readlines():
            reading += line.decode().strip()
        if reading.strip() == "":
            return ""
        return json.loads(reading)
    
    def write(self, msg):
        if msg.startswith("servo "):
            degree = int(msg.split(" ")[1])
            if degree <= 180 and degree >= 0:
                self.ser.write(b"servo %d   \n" % degree)
            else:
                print("Invalid degree for servo")
        elif msg == "fan on":
            self.ser.write(b"fan on\n")
        elif msg == "fan off":
            self.ser.write(b"fan off\n")
        elif msg == "cooler on":
            self.ser.write(b"cooler on\n")
        elif msg == "cooler off":
            self.ser.write(b"cooler off\n")
        else:
            print("invalid arduinoSerial.write argument: " + msg)

    def rotate_servo(self, degree):
        self.write("servo " + str(degree))

if __name__ == '__main__':
    arduino = ArduinoSerial()
    number = 0
    while True:
        reading = arduino.read()
        if reading != "":
            print(reading)
        time.sleep(1)
        arduino.rotate_servo(number)
        time.sleep(4)
        number += 45