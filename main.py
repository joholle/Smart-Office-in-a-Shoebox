import serial

# listen and send commands to arduino serial port 9600
ser = serial.Serial('COM3', 9600, timeout=0.1)
while True:
    command = input()
    if command == "read":
        ser.write(b"read\n")
        for line in ser.readlines():
            print(line.decode().strip())
    elif command.startswith("servo "):
        degree = int(command.split(" ")[1])
        ser.write(b"servo %d\n" % degree)
    elif command == "exit":
        break