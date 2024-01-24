//   #include <Servo.h>

// Servo servo1;
// //Servo servo2;

// void setup() {
  
//   servo1.attach(9); // Attach servo 1 signal pin to D2
//   //servo2.attach(D2); // Attach servo 2 signal pin to D4
//   Serial.begin(9600);
// }

// void loop() {
//   if (Serial.available() > 0) {
//     char command = Serial.read();
//     int angle;
    
//     // Check the command received and adjust the servo angles accordingly
//     if (command == '1') {
//       servo1.write(0);  // tell servo to go to a particular angle
//       delay(1000);
  
//       servo1.write(90);              
//       delay(500); 
//       // angle = constrain(servo1.read(), 0, 180); // Increase angle by 20 degrees, constrained between 0 and 180
//       // servo1.write(angle);}
      
//     //   else if (command == '2') {
//     //   angle = constrain(servo1.read() - 20, 0, 180 ); // Decrease angle by 20 degrees, constrained between 0 and 180
//     //   servo1.write(angle);
//     // } else if (command == '3') {
//     //   angle = constrain(servo2.read() + 20, 0, 180); // Increase angle by 20 degrees, constrained between 0 and 180
//     //   servo2.write(angle);
//     // } else if (command == '4') {
//     //   angle = constrain(servo2.read() - 20, 0, 180); // Decrease angle by 20 degrees, constrained between 0 and 180
//     //   servo2.write(angle);
//     }
//   }
//   delay(10); // Small delay to prevent excessive loop execution
// }

#include <Servo.h>

Servo servo1;
int relayPin = 3;  // Replace with the actual GPIO pin number connected to the relay signal


void setup() {
  servo1.attach(9);  // Attach servo 1 signal pin to D2
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Check the command received and adjust the servo angles accordingly
    if (command == '1') {
      digitalWrite(relayPin, HIGH);  // Turn on the relay
      delay(100);
      servo1.write(- 110);
      delay(1000);
      servo1.write(110);
      delay(500);
      digitalWrite(relayPin, LOW);
      delay(500);
      digitalWrite(relayPin, HIGH);  // Turn on the relay
      delay(100); 
      servo1.write(- 110);
      delay(500);
      servo1.write(110);
      delay(500);
      digitalWrite(relayPin, LOW);
      delay(500);
      digitalWrite(relayPin, HIGH);
      servo1.write(- 60);
      delay(500);
      digitalWrite(relayPin, LOW);
      delay(500);

    }
  }
  delay(10); // Small delay to prevent excessive loop execution
}

// #include <Servo.h>

// Servo servo1;

// void setup() {
//   servo1.attach(9);  // Attach servo 1 signal pin to D9
//   Serial.begin(9600);
// }

// void loop() {
//   if (Serial.available() > 0) {
//     char command = Serial.read();
    
//     // Check the command received and adjust the servo angles accordingly
//     if (command == '1') {
//       // Move the servo by 90 degrees from its current position
//       servo1.write(servo1.read() - 90);
//       delay(2000);
      
//       // Move the servo back to its original position
//       servo1.write(servo1.read() + 90);
//       delay(1000);
//     }
//     else {
//       Serial.println("no command received");
//     }
//   }
  
//   delay(1000); // Small delay to prevent excessive loop execution
// }

