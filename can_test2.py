import can
import time
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=1000000)
#bus = can.interface.Bus(bustype='ixxat', channel='0', bitrate=1000000)
msg = can.Message(arbitration_id=0x140+3, data=[0xA2, 0x00, 0x00, 0x00, 0xD0, 0x09, 0x00, 0x00], is_extended_id=False)
try:
    bus.send(msg)
    print(f"Message sent on {bus.channel_info}")
    print(msg.data)
    print(msg.arbitration_id)
except can.CanError:
    print("Message NOT sent")
    print(can.CanError)
msg = bus.recv(1)
if msg is not None:
    print(msg)
time.sleep(10) 
msg = can.Message(arbitration_id=0x140+3, data=[0xA2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
try:
    bus.send(msg)
    print(f"Message sent on {bus.channel_info}")
    print(msg.data)
    print(msg.arbitration_id)
except can.CanError:
    print("Message NOT sent")
    print(can.CanError)
msg = bus.recv(1)
if msg is not None:
    print(msg)
msg = can.Message(arbitration_id=0x140+1, data=[0xA2, 0x00, 0x00, 0x00, 0xD0, 0x09, 0x00, 0x00], is_extended_id=False)
try:
    bus.send(msg)
    print(f"Message sent on {bus.channel_info}")
    print(msg.data)
    print(msg.arbitration_id)
except can.CanError:
    print("Message NOT sent")
    print(can.CanError)
msg = bus.recv(1)
if msg is not None:
    print(msg)
time.sleep(10)
msg = can.Message(arbitration_id=0x140+1, data=[0xA2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
try:
    bus.send(msg)
    print(f"Message sent on {bus.channel_info}")
    print(msg.data)
    print(msg.arbitration_id)
except can.CanError:
    print("Message NOT sent")
    print(can.CanError)
msg = bus.recv(1)
if msg is not None:
    print(msg)
