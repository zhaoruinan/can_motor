import can
#bus = can.interface.Bus(bustype='kvaser', channel='can0', bitrate=57600)
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=125000)
#msg = can.Message(arbitration_id=0x03+node,data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],is_extended_id=False)
#    bus.send(msg)
msg = can.Message(
            #arbitration_id=0xC0FFEE, data=[0x3E, 0xA2, 0x03, 0x04, 0xE7, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False
            #arbitration_id=3, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False
            arbitration_id=0x140+3, data=[0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=True
            #arbitration_id=3, data=[0x3E, 0xA2, 0x03, 0x04, 0xE7, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False
            )

try:
    bus.send(msg)
    print(f"Message sent on {bus.channel_info}")
    print(msg.data)
    print(msg.arbitration_id)
except can.CanError:
    print("Message NOT sent")
    print(can.CanError)
try:
     while True:
         msg = bus.recv(1)
         if msg is not None:
             print(msg)
except KeyboardInterrupt:
    pass  # exit normally