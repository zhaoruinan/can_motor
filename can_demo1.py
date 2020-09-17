import can
import time
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=1000000)
def motor_set_speed(node,speed):
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00, 0x00+speed, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)
def motor_set_speed_m3(node):
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x10, 0xFA, 0xFF, 0xFF], is_extended_id=False)
    bus.send(msg)
motor_set_speed(1,6)
time.sleep(6)
motor_set_speed(1,0)
motor_set_speed(3,6)
time.sleep(6)
motor_set_speed(3,0)
motor_set_speed_m3(1)
time.sleep(5)
motor_set_speed(1,0)
motor_set_speed_m3(3)
time.sleep(5)
motor_set_speed(3,0)