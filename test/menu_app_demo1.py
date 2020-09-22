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
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))
        panel = wx.Panel(frame, -1)
        self.button1 = wx.Button(panel,-1,'Stop1',pos = (30,80))
        self.button2 = wx.Button(panel,-1,'move1',pos = (30,120))
        self.button3 = wx.Button(panel,-1,'move1-',pos = (30,40))
        self.Bind(wx.EVT_BUTTON, self.OnButton1,self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2,self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnButton3,self.button3)
        
        self.button1_1 = wx.Button(panel,-1,'Stop2',pos = (120,80))
        self.button2_1 = wx.Button(panel,-1,'move2+',pos = (120,120))
        self.button3_1 = wx.Button(panel,-1,'move2-',pos = (120,40))
        self.Bind(wx.EVT_BUTTON, self.OnButton1_1,self.button1_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2_1,self.button2_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton3_1,self.button3_1)
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
        
app = MyApp()
app.MainLoop()
        
