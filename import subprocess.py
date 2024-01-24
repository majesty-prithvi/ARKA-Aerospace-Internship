import subprocess
import serial
import time

arduino_port = 'COM13'  

def send_command_to_arduino(command):
    ser = serial.Serial(arduino_port, 9600, timeout=1)
    ser.write(command.encode())
    ser.close()

# def simulate_keypress(key):
#     subprocess.run(['xdotool', 'key', '--clearmodifiers', key])
    
try:
    while True:
        
        # simulate_keypress('Up')
        send_command_to_arduino('1')
        print('1')
        time.sleep(20)   # Add a delay to prevent multiple presses within a short time
    
      

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    pass
