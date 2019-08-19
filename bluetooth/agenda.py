# Importing the Bluetooth Socket library
from bluetooth import *

from time import sleep

from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(('',PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = '94f39d29-7d6d-437d-973b-fba39e49d4ee'

advertise_service( server_sock, 'SampleServer',
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
                   #protocols = [ OBEX_UUID ] 
                    )
                   
print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        # Receivng the data. 
        data = client_sock.recv(1024) # 1024 is the buffer size.
        data = str(data,"utf-8")
        if data == '11':
            while true:
                print ((data))
                #if len(data) != 0: break

        else:
            print (data)
       
        client_sock.send('send_data')
        sleep(1)
except:
    print('disconnected')
    # Closing the client and server connection
    client_sock.close()
    server_sock.close()
    print("all done")
