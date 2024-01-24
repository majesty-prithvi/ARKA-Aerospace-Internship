#include <Servo.h>

Servo servo1;
int inputPin = 2;  // Replace with the actual GPIO pin number connected to the high signal
int relayPin = 3;  // Replace with the actual GPIO pin number connected to the relay signal

void setup() {
  servo1.attach(9);  // Attach servo 1 signal pin to D9
  pinMode(inputPin, INPUT);
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  if (digitalRead(inputPin) == HIGH) {
    digitalWrite(relayPin, LOW);  // Turn on the relay
    delay(1000);
    servo1.write(servo1.read() - 110);
    delay(1000);
    servo1.write(servo1.read() + 60);
    delay(2000);
    digitalWrite(relayPin, HIGH);  // Turn off the relay
  delay(300);
  }
}

