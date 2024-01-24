# import paho.mqtt.client as mqtt
# import ssl
# import time

# # Callback when connection to MQTT broker is established
# def on_connect(client, userdata, flags, rc, properties=None):
#     print(f"Connected with result code {rc}")
#     # Subscribe to the topic where the Raspberry Pi will publish messages
#     client.subscribe("/pi_topic", qos=1)

# # Callback when a message is received from the Raspberry Pi
# def on_message(client, userdata, msg):
#     print(f"Received message from Raspberry Pi: {msg.payload}")
#     # Process the received message and send a response back to the Raspberry Pi
#     response = "Response from PC"
#     client.publish("/pc_topic", payload=response, qos=1)

# # Create an MQTT client instance
# client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
# client.on_connect = on_connect
# client.on_message = on_message
# client.tls_set(tls_version=ssl.PROTOCOL_TLS)
# client.username_pw_set("ARKA2", "Arka@12345")

# client.connect("a17198ec2202427397984b26070c7dad.s1.eu.hivemq.cloud", 8883)
# # Connect to the MQTT broker

# # Start the MQTT client loop in a separate thread
# client.loop_start()

# try:
#     while True:
#         # Your PC code logic goes here
#         time.sleep(1)

# except KeyboardInterrupt:
#     client.loop_stop()
#     client.disconnect()

import time
import paho.mqtt.client as mqtt
import ssl

# Callback when connection to MQTT broker is established
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

# Callback when a message is received from the Raspberry Pi
def on_message(client, userdata, msg):
    print(f"Received message from Raspberry Pi: {msg.payload.decode()}")
    # Process the received message and send a response back to Raspberry Pi
    response = "Response from PC"
    client.publish("/pc_topic", payload=response, qos=1)

# Create an MQTT client instance
client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set("ARKA2", "Arka@12345")  # Replace with your HiveMQ Cloud username and password

# Connect to the MQTT broker
client.connect("a17198ec2202427397984b26070c7dad.s1.eu.hivemq.cloud", 8883)  # Replace with your HiveMQ Cloud broker address

# Set up the MQTT subscriber
client.subscribe("/pi_topic", qos=1)

# Start the MQTT client loop in a separate thread
client.loop_start()

try:
    #while True:
        # Your PC code logic goes here
    message = "Yo Yo"
    client.publish("/pc_topic", payload=message, qos=1)
    time.sleep(1)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
