import socket
import threading
from datetime import datetime
import time
from ctypes import *
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9911        # Port to listen on (non-privileged ports are > 1023)
SIZE_DATA_ASCII_MAX = 32
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("double6dArr", c_double * 6),("bool", c_bool * 8)]
#from motor_can import motor_set_speed,motor_set_speed_m,motor_read_pos
def server():
    write_buffer = (c_char* 1024)()
    read_buffer = (c_char* 1024)()
    res_data = Data()    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            send_data = Data()
            while True:
                read_buffer = conn.recv(1024)
                #if not read_buffer:
                #    break
                print('send data  ',send_data.double6dArr[5])
                memmove(res_data.byte, read_buffer, 1024)
                print('receive data  ',res_data.double6dArr[5])
                print('speed1  ',res_data.double6dArr[0])
                print('speed2 ',res_data.double6dArr[1])                
                print("server",datetime.fromtimestamp(time.time()))                                
                #motor_set_speed,motor_set_speed_m
                #motor_read_pos
                send_data.double6dArr[5] =0.002 +send_data.double6dArr[5]
                memmove( write_buffer,send_data.byte ,1024)
                print('send data  ',send_data.double6dArr[5])
                conn.sendall(write_buffer)
                time.sleep(0.2)           
def main():
    server()
#if __name__ =='__main__':
main()