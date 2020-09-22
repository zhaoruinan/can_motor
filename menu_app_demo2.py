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
def motor_set_speed(node,speed):
    n = speed*100
    b = int_to_char(n)
    print(b)
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00+b[3], 0x00+b[2], 0x00+b[1], 0x00+b[0]], is_extended_id=False)
    bus.send(msg)
def motor_set_speed_m(node,speed):
    n = -speed*100
    b = int_to_char(n)
    print(b)
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00+b[3], 0x00+b[2], 0x00+b[1], 0x00+b[0]], is_extended_id=False)
    bus.send(msg)
def motor_read_pos(node):
    msg = can.Message(arbitration_id=0x140+node, data=[0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)
    recv = bus.recv()
    print(recv)
    try:
        return(recv.data[3]*256+recv.data[2])
    except:
        print("please make sure CAN cable is working")
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
        motor_set_speed(1,0)
        
    def OnButton2(self, event):
        motor_set_speed(1,self.speed1)
    
    def OnButton3(self, event):
        motor_set_speed_m(1,self.speed1)

    def OnButton1_1(self, event):
        motor_set_speed(3,0)
        
    def OnButton2_1(self, event):
        motor_set_speed(3,self.speed3)
    
    def OnButton3_1(self, event):
        motor_set_speed_m(3,self.speed3)

    def OnUpdate(self, event):
        pos1 = motor_read_pos(1)
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
app = MyApp()
app.MainLoop()