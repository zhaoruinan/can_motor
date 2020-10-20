import socket
from datetime import datetime
import time
from ctypes import *
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

SIZE_DATA_ASCII_MAX = 32
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("double6dArr", c_double * 6)]

#from motor_can import motor_set_speed,motor_set_speed_m,motor_read_pos
def data_process(data):
    return True
def server(s,send_data):
    write_buffer = (c_char* 1024)()
    read_buffer = (c_char* 1024)()
    res_data = Data()
    
    
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
            print('Connected by', addr)
            read_buffer = conn.recv(1024)
                #if not read_buffer:
                #    break
            print('send data  ',send_data.double6dArr[5])
            memmove(res_data.byte, read_buffer, 1024)
            print('receive data  ',res_data.double6dArr[5])
            
            print("server",datetime.fromtimestamp(time.time()))
                
                
                #motor_set_speed,motor_set_speed_m
                #motor_read_pos
            send_data.double6dArr[5] =0.002 +send_data.double6dArr[5]
            memmove( send_data.byte ,write_buffer,1024)
            print('send data  ',send_data.double6dArr[5])
            conn.sendall(write_buffer)
            time.sleep(0.2)
            return res_data
def main():
    send_data = Data()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        send_data.double6dArr[5] = 0.002 +send_data.double6dArr[5]

        res_data = server(s,send_data)


#if __name__ =='__main__':
main()