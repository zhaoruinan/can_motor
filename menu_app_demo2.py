import wx
import can
import time
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=1000000)
def motor_set_speed(node,speed):
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00, 0x00+speed, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)
def motor_set_speed_m(node):
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x90, 0xFF, 0xFF, 0xFF], is_extended_id=False)
    bus.send(msg)
def motor_read_pos(node):
    msg = can.Message(arbitration_id=0x140+node, data=[0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)
    recv = bus.recv()
    print(recv)
    return(recv.data[3]*256+recv.data[2])
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'wxPython',size = (280,360))
        panel = wx.Panel(frame, -1)
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

        self.label3 = wx.StaticText(panel,-1, "Pos(0.01rad)",pos = (30,210))
        self.text3 = wx.TextCtrl(panel, -1,pos = (30,230),size = (80,-1),style = wx.TE_READONLY)
        self.label4 = wx.StaticText(panel,-1, "Pos(0.01rad)",pos = (150,210))
        self.text4 = wx.TextCtrl(panel, -1,pos = (150,230),size = (80,-1),style = wx.TE_READONLY)

        self.button4 = wx.Button(panel,-1,'update',pos = (30,270))
        self.Bind(wx.EVT_BUTTON, self.OnButton4,self.button4)
        frame.Show()
        return True
    def OnButton1(self, event):
        motor_set_speed(1,0)
        
    def OnButton2(self, event):
        motor_set_speed(1,2)
    
    def OnButton3(self, event):
        motor_set_speed_m(1)

    def OnButton1_1(self, event):
        motor_set_speed(3,0)
        
    def OnButton2_1(self, event):
        motor_set_speed(3,2)
    
    def OnButton3_1(self, event):
        motor_set_speed_m(3)

    def OnButton4(self, event):
        pos1 = motor_read_pos(1)
        pos2 = motor_read_pos(3)
        print(pos1,pos2)
        self.text3.SetValue(str(pos1))
        self.text4.SetValue(str(pos2))

    def OnText1(self, event):
        motor_read_pos(1)
        motor_read_pos(3)        
app = MyApp()
app.MainLoop()
        
