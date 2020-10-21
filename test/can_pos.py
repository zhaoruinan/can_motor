import wx
import can
import time
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=1000000)
def int_to_char(n):
    b = [0x00, 0x00, 0x00, 0x00]
    b[0] =b[0]+ ((n & 0xff000000) >> 24)
    b[1] =b[1]+ ((n & 0xff0000) >> 16)
    b[2] =b[2]+ ((n & 0xff00) >> 8)
    b[3] =b[3]+ (n & 0xff)
    return b
class motor:
    def __init__(self,node):
        self.node = node
    def motor_set_speed(node,speed):
        n = speed*100
        b = int_to_char(n)
        print(b)
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00+b[3], 0x00+b[2], 0x00+b[1], 0x00+b[0]], is_extended_id=False)
    bus.send(msg)
    def motor_set_pos(self,pos):
        pos = pos*100
        b = int_to_char(n)
        print(b)
        msg = can.Message(arbitration_id=0x140+self.node, data=[0xA2, 0x00, 0x00, 0x00, 0x00+b[3], 0x00+b[2], 0x00+b[1], 0x00+b[0]], is_extended_id=False)
        bus.send(msg)
    def motor_read_pos(self):
        msg = can.Message(arbitration_id=0x140+self.node, data=[0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
        bus.send(msg)
        recv = bus.recv()
        print(recv)
        try:
            return(recv.data[3]*256+recv.data[2])
        except:
            print("please make sure CAN cable is working")
def main():
    motor1 = motor(3)
    motor2 = motor(5)
    
#if __name__ =='__main__':
main()