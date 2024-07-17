# Smart Office in a Shoebox
**Abstract:** The "Smart Office in a Shoebox" project aims to demonstrate how Internet of Things (IoT) devices and Artificial Intelligence (AI) can enhance the energy efficiency and comfort of office environments. This system integrates various sensors, including those for brightness, temperature, humidity, and water, to control actuators like lights, fans, and a cooling pad. The architecture includes an Arduino for low-level processing and a Raspberry Pi for higher-level functions, with AI planning facilitated by a connected laptop. User interfaces allow for real-time monitoring and manual interventions, ensuring flexibility and responsiveness. Prioritizing user comfort, energy savings, and system reliability, the project highlights how smart technologies can create healthier, more sustainable office spaces. Through the implementation and testing of this scaled-down model, the smart office in a shoebox demonstrates the potential for broader application of IoT and AI in actual office settings, aiming to reduce the substantial energy consumption and enhance the wellbeing of office workers.
For more information, visit [report.pdf](report.pdf)

## Requirements:
Devices:
 - Power supply (5V 2-3A)
 - Arduino
 - Raspberry Pi
 - Laptop

Sensors:
 - DHT 11 temperature and humidity sensor
 - ARD SEN WET2 water sensor
 - Photoresistor GL5528

Actuators:
 - SG90 9g micro servo
 - 4 LED (3.3V white)
 - Fan (5V)
 - TEC1-12706 Cooling Pad

Other:
 - 220Ω Resistor

TODO: Soldering sketch

## Setup
1. Pi:
 - Install and setup Mosquitto
 - pip install pyvenv
 - python -m venv env
 - source env/bin/activate    - for Linux
 - pip install pyserial, mqtt
2. Laptop:
 - Install and setup Mosquitto
 - pip install pyvenv
 - python -m venv env
 - source env/bin/activate     - for Linux
 - pip install pddl, mqtt, tkinter

## Run Program
1. Pi:
 - nohup mosquitto -v &
 - source env/bin/activate     - for Linux
 - python main.py
2. Laptop:
 - source env/bin/activate     - for Linux
 - python main-laptop.py
