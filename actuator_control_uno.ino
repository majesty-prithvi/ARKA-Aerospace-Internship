// needs more changes for working. basically takes serial (1 or 0 input) from keyboard and extends and retracts the actuator accordingly


void setup() {
  pinMode(7, OUTPUT); // Configure pin 7 as an Output
  pinMode(8, OUTPUT); // Configure pin 8 as an Output

  digitalWrite(7, HIGH); // Initialize pin 7 as Low
  digitalWrite(8, HIGH); // Initialize pin 8 as Low
}

void loop() {
  // Extend Linear Actuator
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Check the command received and adjust the servo angles accordingly
    if (command == '1') {
      // Move the actuator to extend position
      digitalWrite(7, LOW);
      digitalWrite(8, HIGH);

      delay(2000); // 2 seconds
  
      // Stop Actuator
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);

      delay(2000); // 2 seconds
    }
    // Retract Linear Actuator
    else if (command == '0') {
      // Move the actuator to retract position
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);

      delay(2000); // 2 seconds
  
      // Stop Actuator
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);

      delay(2000); // 2 seconds
    }
  }
}