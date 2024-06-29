#include <DHT.h>
// install the library: dht sensor library by Adafruit

#define DHTPIN 2
#define DHTTYPE DHT11

int pin = 2;
DHT dht(DHTPIN, DHTTYPE);

// 5V -> +
// A0 -> out
// gnd -> -

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  if (!isnan(t) && !isnan(h)) {
    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.print(", Humidity: ");
    Serial.print(h);
    Serial.println("%");
  }
  delay(2000);
}
