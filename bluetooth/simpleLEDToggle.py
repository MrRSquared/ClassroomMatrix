# Importing the Bluetooth Socket library
import bluetooth
# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO
from time import sleep

led_pin = 21    # Initializing pin 40 for led
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
GPIO.setup(led_pin, GPIO.OUT)   # Declaring the pin 40 as output pin

host = ""
port = 1    # Raspberry Pi uses port 1 for Bluetooth Communication

# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')

try:
    server.bind((host, port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")

server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address. 
client, address = server.accept()
print("Connected To", address)
print("Client:", client)

try:
    while True:
        # Receivng the data. 
        data = client.recv(2048) # 1024 is the buffer size.
        
        sleep(1)
        print(data)
        
        if data == b'1':
            GPIO.output(led_pin, True)
            send_data = "Light On "
        elif data == b'0':
            GPIO.output(led_pin, False)
            send_data = "Light Off "
        else:
            send_data = "Type 1 or 0 "

        # Sending the data.
        client.send(send_data)
        sleep(1)
except:
    # Making all the output pins LOW
    GPIO.cleanup()
    # Closing the client and server connection
    client.close()
    server.close()