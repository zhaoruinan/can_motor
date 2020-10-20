# #!/usr/bin/env python3
HOST = '127.0.0.1'  # The server's hostname or IP address
#HOST = '192.168.0.100'  # The server's hostname or IP address
PORT = 9911        # The port used by the server
SIZE_DATA_TCP  = 200
SIZE_DATA_MAX = 200
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))

# import socket, time
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))
# print client.send('Hello world!'), 'bytes sent.'
# time.sleep(0.2)
# print 'Received message:', client.recv(1024)

# class TCP_Client:
# 	def 

import socket, time
from ctypes import *
SIZE_DATA_ASCII_MAX = 32
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("double6dArr", c_double * 6)]


def client():    
	write_buffer = (c_char* 1024)()
	read_buffer = (c_char* 1024)()
	res_data = Data()
	send_data = Data()
	send_data.double6dArr[0] = 0.001
	while True:
		send_data.double6dArr[1] +=0.001
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))
		memmove(write_buffer, send_data.byte ,1024)
		client.send(write_buffer), 'bytes sent.'
		#time.sleep(0.2)
		read_buffer = client.recv(1024)
		memmove(res_data.byte, read_buffer, 1024)
		print('send data  ',send_data.double6dArr[5])
		print('receive data  ',res_data.double6dArr[5])
	#print 'Received message:', read_buffer

#if __name__ =='__main__':


client()