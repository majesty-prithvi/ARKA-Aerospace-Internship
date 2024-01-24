# import serial
# import keyboard
# import time

# # Replace 'COM5' with your Arduino's serial port and 9600 with the appropriate baud rate
# ser = serial.Serial('COM4', 9600, timeout=1)

# def move_servo(rotate):
#     command = f"{rotate}\n"
#     ser.write(command.encode())
#     time.sleep(0.2)  # Wait for the servo to move, adjust if necessary

# try:
#     while True:
#         if keyboard.is_pressed('x'):
#             move_servo('1')  # Rotate the servo when 'x' key is pressed
#             time.sleep(0.2)   # Add a delay to prevent multiple presses within a short time
#         elif keyboard.is_pressed('y'):
#             move_servo('0')
# except KeyboardInterrupt:
#     ser.close()  # Close the serial port when the program is interrupted

import serial
import keyboard
import time

# Replace 'COM4' with your Arduino's serial port and 9600 with the appropriate baud rate
ser = serial.Serial('COM13', 9600, timeout=1)
print('START')

def move_servo(direction):
    command = f"{direction}\n"
    ser.write(command.encode())
    time.sleep(0.2)  # Wait for the servo to move, adjust if necessary

try:
    while True:
        if keyboard.is_pressed('x'):
            print('UP')
            move_servo('1')  # Rotate the servo when 'x' key is pressed
            time.sleep(1)   # Add a delay to prevent multiple presses within a short time
        # elif keyboard.is_pressed('y'):
            move_servo('0')
            print('DOWN')
            time.sleep(1)
except KeyboardInterrupt:
    ser.close()  # Close the serial port when the program is interrupted

