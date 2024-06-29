#include <Servo.h>

int pin = 4;
Servo servo;

// Circuit:
// 5V -> +
// A0 -> S
// gnd -> -

// < 100 with no water
// ~ 500 with water

void setup() {
  Serial.begin(9600);
  servo.attach(pin);
}

void loop() {
  for (int i = 0; i < 30; i++) {
    servo.write(i*60);
    delay(100);
  }
}
