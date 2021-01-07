import socket
from socket import error as SocketError
import errno
import threading
from threading import Lock
from datetime import datetime
import time
from ctypes import *
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2056        # The port used by the server
SIZE_DATA_ASCII_MAX = 32
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("double6dArr", c_double * 6),("boolArr", c_bool * 8)]
global send_data,res_data,send_data_dou,send_data_b
send_data = Data()
res_data = Data()
res_data.double6dArr[0] = 0.0
res_data.double6dArr[1] = 0.0
lock = Lock()
def tcp_client(s):
    global send_data,res_data,send_data_dou,send_data_b
    lock.acquire()
    write_buffer = (c_char* 1024)()  
    memmove( write_buffer, send_data.byte,1024)
    lock.release()
    s.sendall(write_buffer)
    start = datetime.now()
    #if res_data.double6dArr[0]:
    #    print('neck2cam',tf_neck2cam(res_data.double6dArr[0],res_data.double6dArr[1]))
    end = datetime.now()
    exec_time = end - start
    print(exec_time,exec_time.total_seconds())
    time.sleep(0.2-exec_time.total_seconds())

def socket_tcp():
    global send_data,res_data,send_data_dou,send_data_b,sim_v1,sim_v2 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    send_data_b = [0.6666,0.77777]
    while True:
        #lock.acquire()
        send_data.double6dArr[5] = 0.001 +send_data.double6dArr[5]
        
        send_data.boolArr[0]= send_data_b[0]
        
        send_data.boolArr[1]= send_data_b[1]
        sim_v1 = send_data.double6dArr[0]
        sim_v2 = send_data.double6dArr[1]
        tcp_client(s)
def main():
    t_tcp = threading.Thread(target=socket_tcp)
    t_tcp.start()
#if __name__ =='__main__':
main()