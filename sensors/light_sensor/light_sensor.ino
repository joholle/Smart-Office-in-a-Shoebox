int pin = A0;

// Circuit:
// 5V -> photoresistorA
// photoresistorB -> A0 and 330R
// 330R -> gnd

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(pin);
  Serial.print("Light sensor: ");
  Serial.println(value);
  delay(100);
}
