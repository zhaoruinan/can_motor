import wx
import socket
from socket import error as SocketError
import errno
import threading
from datetime import datetime
import time
from ctypes import *
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9911        # The port used by the server
SIZE_DATA_ASCII_MAX = 32
SIZE_DATA_TCP_MAX  = 200
class Data(Union):
    _fields_ = [("byte", c_ubyte * SIZE_DATA_TCP_MAX),("double6dArr", c_double * 6)]
#print('Received', repr(data))
def socket_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    send_data = Data()
    s.connect((HOST, PORT))
    while True:
        send_data.double6dArr[5] = 0.001 +send_data.double6dArr[5] 
        tcp_client(s,send_data)
       

def tcp_client(s,send_data):
    write_buffer = (c_char* 1024)()
    #read_buffer = (c_char* 1024)()
    res_data = Data()  
    #print('send data  ',send_data.double6dArr[5])  
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


    memmove( write_buffer, send_data.byte,1024)
    s.sendall(write_buffer)
    time.sleep(0.2)
    read_buffer = s.recv(1024)
    memmove( res_data.byte,read_buffer, 1024)
    print('receive data  ',res_data.double6dArr[5])
    print("client",datetime.fromtimestamp(time.time()))
    print('send data  ',send_data.double6dArr[5])

        #print('Received', repr(data))
    return res_data
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'wxPython',size = (280,360))
        panel = wx.Panel(frame, -1)
        self.speed1, speed3 = 0,0
        self.button1 = wx.Button(panel,-1,'Stop1',pos = (30,80))
        self.button2 = wx.Button(panel,-1,'move1',pos = (30,120))
        self.button3 = wx.Button(panel,-1,'move1-',pos = (30,40))
        self.Bind(wx.EVT_BUTTON, self.OnButton1,self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2,self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnButton3,self.button3)
        
        self.button1_1 = wx.Button(panel,-1,'Stop2',pos = (150,80))
        self.button2_1 = wx.Button(panel,-1,'move2+',pos = (150,120))
        self.button3_1 = wx.Button(panel,-1,'move2-',pos = (150,40))
        self.Bind(wx.EVT_BUTTON, self.OnButton1_1,self.button1_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2_1,self.button2_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton3_1,self.button3_1)

        self.label1 = wx.StaticText(panel,-1, "speed(0.01rad)",pos = (30,160))
        self.text1 = wx.TextCtrl(panel, -1,pos = (30,180),size = (80,-1))
        self.Bind(wx.EVT_TEXT, self.OnText1, self.text1)  
        self.label2 = wx.StaticText(panel,-1, "speed(0.01rad)",pos = (150,160))
        self.text2 = wx.TextCtrl(panel, -1,pos = (150,180),size = (80,-1))
        self.Bind(wx.EVT_TEXT, self.OnText2, self.text2)  

        self.label3 = wx.StaticText(panel,-1, "Pos(0.01rad)",pos = (30,210))
        self.text3 = wx.TextCtrl(panel, -1,pos = (30,230),size = (80,-1),style = wx.TE_READONLY)
        self.label4 = wx.StaticText(panel,-1, "Pos(0.01rad)",pos = (150,210))
        self.text4 = wx.TextCtrl(panel, -1,pos = (150,230),size = (80,-1),style = wx.TE_READONLY)

        self.update_button = wx.Button(panel,-1,'update',pos = (30,270))
        self.Bind(wx.EVT_BUTTON, self.OnUpdate,self.update_button)
        self.text1.SetValue('0')
        self.text2.SetValue('0')
        frame.Show()
        return True
    def OnButton1(self, event):
        motor_set_speed(5,0)
        pos = motor_read_pos(5)
        #print(pos)
        self.text3.SetValue(str(pos))
        
    def OnButton2(self, event):
        motor_set_speed(5,self.speed1)
    
    def OnButton3(self, event):
        motor_set_speed_m(5,self.speed1)

    def OnButton1_1(self, event):
        motor_set_speed(3,0)
        pos = motor_read_pos(3)
        #print(pos)
        self.text4.SetValue(str(pos))
        
    def OnButton2_1(self, event):
        motor_set_speed(3,self.speed3)
    
    def OnButton3_1(self, event):
        motor_set_speed_m(3,self.speed3)

    def OnUpdate(self, event):
        pos1 = motor_read_pos(5)
        pos2 = motor_read_pos(3)
        #print(pos1,pos2)
        self.text3.SetValue(str(pos1))
        self.text4.SetValue(str(pos2))
    def OnText1(self, event):
        text = self.text1.GetValue()
        try:
            print(int(text))
            self.speed1 = int(text)
        except:
            self.text1.SetValue('0')
    def OnText2(self, event):
        text = self.text2.GetValue()
        try:
            print(int(text))
            self.speed3 = int(text)
        except:
            self.text2.SetValue('0')
def main():
    t_tcp = threading.Thread(target=socket_tcp)
    t_tcp.start()
    app = MyApp()
    app.MainLoop()
#if __name__ =='__main__':
main()