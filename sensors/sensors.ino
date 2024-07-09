#include <Servo.h>
#include <DHT.h>
#include <ArduinoJson.h>
// install the libraries:
// - dht sensor library by Adafruit
// - servo library by Arduino
// - ArduinoJson by Benoit Blanchon

#define WATER_SENSOR_PIN A0
#define LIGHT_SENSOR_PIN A1
#define SERVO_PIN 3
#define DHT_SENSOR_PIN 2
#define DHTTYPE DHT11


DHT dht(DHT_SENSOR_PIN, DHTTYPE);
Servo servo;
String input = "";
bool string_complete = false;

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
  dht.begin();
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

      serializeJson(doc, Serial);
      Serial.println();
    } else if (input.startsWith("servo ")) {
      int degrees = 
      Serial.println("writing");
    }
    // for (int i = 0; i < 30; i++) {
    //     servo.write(i*60);
    //     delay(100);
    // }

    input = "";
    string_complete = false;
  }
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
