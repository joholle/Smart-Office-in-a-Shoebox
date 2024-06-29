int pin = A0;

// Circuit:
// 5V -> +
// A0 -> S
// gnd -> -

// < 100 with no water
// ~ 500 with water

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(pin);
  Serial.print("Water sensor: ");
  Serial.println(value);
  delay(500);
}
