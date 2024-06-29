import serial, json

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
    
    # def write(self, msg):
    #     if command.startswith("servo "):
    #         degree = int(command.split(" ")[1])
    #         ser.write(b"servo %d\n" % degree)
        