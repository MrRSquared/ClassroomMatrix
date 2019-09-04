#!/usr/bin/env python

"""This is the code is to connect our esp32 to cheerlights.

Our main encoder code is borrowed from Jousef ROusek.  and can be found here https://github.com/stlk/micropython/blob/master/workshop/ """

import socket

url = 'http://api.thingspeak.com/channels/1417/field/2/last.txt'
_, _, host, path = url.split('/', 3)
ai = socket.getaddrinfo(host, 80)
print('Address infos:', ai)
addr = ai[0][-1]

print('Connect address:', addr)
s = socket.socket()
s.connect(addr)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
color = ''
while True:
    data = s.recv(100)
    if data:
        chunk = str(data, 'utf8')
        # print(chunk, end='')
        hash_index = chunk.find('#')
        if hash_index >= 0:
            color = chunk[hash_index + 1: hash_index + 7]
    else:
        break
s.close()
print(color)

__author__ = "Jacob Roth-Ritchie"
__copyright__ = "Copyright 20019, RSquar3dT3ch"
__license__ = "GPL 3.0"
__version__ = ".01"
__maintainer__ = "Jacob Roth-Ritchie"
__email__ = "jrothritchie@hdsd.org"
__status__ = "Development"