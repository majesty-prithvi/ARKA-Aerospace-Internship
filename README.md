## Arka Aerospace's Defence Drone Projects (25/12/2023 - 25/1/2024)__

This repository contains codes developed during my internship for Arka Aerospace. Where I worked on their drone project for the Indian Air Force during the period from 25/12/2023 to 25/1/2024.

### 1. Servo Triggering based on Arduino Uno<br>
#### 1.1 Keyboard input based servo control via Serial port
#### Python code: keyboard_servo_control.py
##### Arduino code: keyboard_servo_control_uno.ino
Make the appropriate connections between the Arduino Uno, relay board, breadboard according to the Arduino code. Use the serial port to power the Arduino and send the serial input. Use an external power supply for high torque servos. Flash the Arduino code onto the Uno board and run the Python code on an appropriate code editor. Give the appropriate key inputs and test the servo.

#### 1.2 Keyboard input based solenoid control via Serial port
This system works similarly to the servo control with some changes to the codes.

#### Python code: keyboard_servo_control.py
#### Arduino code: actuator_control_uno.ino
#### 1.3 Servo control using GPIO pins of Raspberry Pi and Arduino Uno
This system works with Raspberry Pi and Arduino Uno. The Raspberry Pi sends commands to the Uno via GPIO pins. The Pi is connected to a desktop via SSH, and a Python code is run in it to give the command to Uno to trigger the servo at the right instant of time.

#### Python code: RPi_GPIO_servo_control.py<br>
#### Arduino code: pi_uno_servo_control.ino<br>
Make the appropriate connections between the Arduino Uno, relay board, breadboard, and Raspberry Pi according to the Arduino and Python code. When the Python code is run on RPi, a high signal is sent to the Uno board. This high signal is a command for the Uno to trigger the servo.

### 2. Python code for Git Pull operation
This Python code clones a GitHub repo into a file on the Raspberry Pi. It only takes two inputs:

#### repo_url: GitHub repository URL.<br>
#### local_repo_path: Local path on the Raspberry Pi.<br>
Each time this code is run, it updates the local repo file on the Pi if any change is made on the origin GitHub repo (basically performing a Git Pull operation).

#### Python code: git_pull.py

### 3. MQTT
#### 3.1 Basic Subscribe and Publish operation using Raspberry Pi/Nvidia Jetson.

Two codes are used to run MQTT. One code is to publish the information, and the other is to subscribe to the information through the MQTT broker. The above codes also allow for bi-directional communication.

#### Raspberry Pi/Jetson code: mqtt_publish_subscribe_pi_jetson.py<br>

#### PC/Ground station code: mqtt_publish_subscribe_pc.py<br>

#### 3.2 MQTT codes to run internal Python Scripts saved on RPi/Jetson.
The structure of code is similar to the basic Subscribe and publish code of MQTT. A library called subprocess and its modules are used to run Python files on RPi/Jetson. The ground station will send a command, and according to the command given, the respective python will be run on the RPi/Jetson.

#### Raspberry Pi/Jetson code: mqtt_CnC_pc_code.py<br>
#### PC/Ground station code: mqtt_drone_code.py<br>
