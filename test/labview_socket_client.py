import socket
import struct
import random
import time
from datetime import datetime
from ctypes import *
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("int7Arr", c_int * 7),("double6dArr", c_double * 42)]
write_buffer = (c_char* 1024)()  


HOST = '192.168.50.4'  # The server's hostname or IP address
PORT = 8089        # The port used by the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
client.connect(server_address)


send_data = Data()

for x in range(2):
    start = datetime.now()
    #send_data.double6dArr[0]=random.uniform(0, 1)
    send_data.int7Arr[0]=1
    send_data.int7Arr[1]=100
    #send_data.double6dArr[0]=3.3
    memmove( write_buffer, send_data.byte,1024)
    client.sendall(write_buffer)
    end = datetime.now()
    exec_time = end - start
    print(send_data.double6dArr[0])
    print(end)
    #print(exec_time,exec_time.total_seconds())
    #time.sleep(0.2-exec_time.total_seconds())
    #read_buffer = s.recv(1024)
    res = [ord(sub) for sub in  write_buffer[:50]] 
    print(res)