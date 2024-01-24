import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Replace 17 with the actual GPIO pin number you want to use
gpio_pin = 17

# Setup the GPIO pin as an output
GPIO.setup(gpio_pin, GPIO.OUT)

try:
    # Set the GPIO pin to high
    GPIO.output(gpio_pin, GPIO.HIGH)
    print(f"GPIO pin {gpio_pin} set to HIGH")

    # Run your other code or sleep if needed
    time.sleep(10)

finally:
    # Cleanup GPIO settings on script exit
    GPIO.cleanup()
    print("GPIO cleanup completed")
