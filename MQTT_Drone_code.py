import time
import paho.mqtt.client as mqtt
import ssl
import subprocess

# Callback when connection to MQTT broker is established
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

# Callback when a message is received from the PC
def on_message(client, userdata, msg):
    print(f"Received message from PC: {msg.payload.decode()}")
    if msg.payload == b"Hello from PC":
        # Example: Run a predefined script or command
        try:
            subprocess.run(["python3", "/home/animesh/mav_ws/src/anti_drone/servo_trigger_3.py"])
        except Exception as e:
            print(f"Error executing the script: {e}")


# Create an MQTT client instance
client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set("ARKA2", "Arka@12345" )  # Replace with your HiveMQ Cloud username and password

# Connect to the MQTT broker
client.connect("a17198ec2202427397984b26070c7dad.s1.eu.hivemq.cloud", 8883)  # Replace with your HiveMQ Cloud broker address

# Set up the MQTT subscriber
client.subscribe("/pc_topic", qos=1)

# Start the MQTT client loop in a separate thread
client.loop_start()

try:
    while True:
        # Your Raspberry Pi code logic goes here
        message = "Hello from Raspberry Pi"
        client.publish("/pi_topic", payload=message, qos=1)
        time.sleep(1)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
