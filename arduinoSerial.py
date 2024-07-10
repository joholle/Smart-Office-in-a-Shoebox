import serial, json, time

class ArduinoSerial:
    def __init__(self):
        com_port = '/dev/ttyACM0'
        baudrate = 9600
        timeout = 0.1
        # listen and send commands to arduino serial port 9600
        self.serial = serial.Serial(com_port, baudrate, timeout=timeout)

    def read(self):
        reading = ""
        self.serial.write(b"read\n")
        for line in self.serial.readlines():
            reading += line.decode().strip()
        if reading.strip() == "":
            return ""
        return json.loads(reading)
    
    def write(self, msg):
        message_to_arduino = b''
        if msg.startswith("servo "):
            degree = int(msg.split(" ")[1])
            if degree <= 180 and degree >= 0:
                message_to_arduino = ("servo %d   \n" % degree).encode()
            else:
                return print("Invalid degree for servo")
        elif msg in ["fan on", "fan off", "cooler on", "cooler off"]:
            message_to_arduino = ("%s\n" % msg).encode()
        else:
            return print("invalid arduinoSerial.write argument: " + msg)
        
        self.serial.write(message_to_arduino)

    def rotate_servo(self, degree):
        self.write("servo " + str(degree))

if __name__ == '__main__':
    arduino = ArduinoSerial()
    servo_degrees = 0
    while True:
        reading = arduino.read()
        if reading != "":
            print(reading)
        time.sleep(1)
        arduino.rotate_servo(servo_degrees)
        time.sleep(4)
        servo_degrees += 45
        if servo_degrees >= 180:
            servo_degrees = 0