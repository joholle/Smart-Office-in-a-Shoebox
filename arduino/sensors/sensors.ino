#include <Servo.h>
#include <DHT.h>
#include <ArduinoJson.h>
// install the libraries:
// - dht sensor library by Adafruit
// - servo library by Arduino
// - ArduinoJson by Benoit Blanchon

#define WATER_SENSOR_PIN A0
#define LIGHT_SENSOR_PIN A1
#define DHT_SENSOR_PIN 2
#define SERVO_PIN 3
#define COOLER_PIN 4
#define FAN_PIN 5
#define LIGHT_PIN 6
#define DHTTYPE DHT11


DHT dht(DHT_SENSOR_PIN, DHTTYPE);
Servo servo;
String input = "";
bool string_complete = false;
int servo_degree = 0;
bool is_fan_active = false;
bool is_cooler_active = false;
bool is_lights_on = false;

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
  servo.write(servo_degree);
  delay(100);
  dht.begin();

  pinMode(COOLER_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(LIGHT_PIN, OUTPUT);
  digitalWrite(COOLER_PIN, LOW);
  digitalWrite(FAN_PIN, LOW);
  digitalWrite(LIGHT_PIN, LOW);
}

void loop() {
  if (string_complete) {
    if (input == "read\n") {
      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();
      int light = analogRead(LIGHT_SENSOR_PIN);
      int water = analogRead(WATER_SENSOR_PIN);

      JsonDocument doc;
      doc["temperature"] = isnan(temperature) ? -1 : temperature;
      doc["humidity"] = isnan(humidity) ? -1 : humidity;
      doc["light"] = light;
      doc["water"] = water;
      doc["servo"] = servo_degree;
      doc["fan"] = is_fan_active;
      doc["cooler"] = is_cooler_active;
      doc["lights"] = is_lights_on;

      serializeJson(doc, Serial);
      Serial.println();
    } else if (input.startsWith("servo ")) {
      servo_degree = input.substring(6, 10).toInt();
      servo.write(servo_degree);
      delay(100);
    } else if (input == "fan on\n") {
      is_fan_active = true;
      digitalWrite(FAN_PIN, HIGH);
    } else if (input == "fan off\n") {
      is_fan_active = false;
      digitalWrite(FAN_PIN, LOW);
    } else if (input == "cooler on\n") {
      is_cooler_active = true;
      digitalWrite(COOLER_PIN, HIGH);
    } else if (input == "cooler off\n") {
      is_cooler_active = false;
      digitalWrite(COOLER_PIN, LOW);
    } else if (input == "lights on\n") {
      is_lights_on = true;
      digitalWrite(LIGHT_PIN, HIGH);
    } else if (input == "lights off\n") {
      is_lights_on = false;
      digitalWrite(LIGHT_PIN, LOW);
    }

    input = "";
    string_complete = false;
  }
  // Test servo functionality
  // for (int i = 0; i < 30; i++) {
  //     servo.write(i*60);
  //     delay(100);
  // }
}

void serialEvent() {
  while (Serial.available()) {
    char in_char = (char) Serial.read();
    input += in_char;
    if (in_char == '\n') {
      string_complete = true;
    }
  }
}

/// Circuits:
// DHT11:
// 5V -> +
// 2 -> out
// gnd -> -
//
// Light Sensor:
// 5V -> photoresistorA
// photoresistorB -> A1 and 330R
// 330R -> gnd
//
// Water Sensor:
// 5V -> +
// A0 -> S
// gnd -> -
//
// Servo:
// 3 -> yellow
// 5V -> red
// gnd -> brown

// < 100 with no water
// ~ 500 with water
