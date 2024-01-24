#include <Servo.h>

Servo servo1;

void setup() {
  servo1.attach(9);  // Attach servo 1 signal pin to D9
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Check the command received and adjust the servo angles accordingly
    if (command == '1') {
      // Move the servo by 90 degrees from its current position
      servo1.write(servo1.read() - 90);
      delay(2000);
      
      // Move the servo back to its original position
      servo1.write(servo1.read() + 90);
      delay(1000);
    }
    else {
      Serial.println("no command received");
    }
  }
  
  delay(1000); // Small delay to prevent excessive loop execution
}

