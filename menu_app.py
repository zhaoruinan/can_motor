import wx
import can
import time
bus = can.interface.Bus(bustype='kvaser', channel='0', bitrate=1000000)
def motor_set_speed(node,speed):
    msg = can.Message(arbitration_id=0x140+node, data=[0xA2, 0x00, 0x00, 0x00, 0x00, 0x00+speed, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))
        panel = wx.Panel(frame, -1)
        self.button1 = wx.Button(panel,-1,'Stop',pos = (120,80))
        self.button2 = wx.Button(panel,-1,'move',pos = (120,120))
        self.Bind(wx.EVT_BUTTON, self.OnButton1,self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2,self.button2)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
        l4 = wx.StaticText(panel, -1, "只读取文本") 
        hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t4 = wx.TextCtrl(panel, value = "只读文本",style = wx.TE_READONLY|wx.TE_CENTER) 
        hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox4)
        panel.SetSizer(vbox) 
        frame.Show()
        return True
    def OnButton1(self, event):
        motor_set_speed(1,0)
        
    def OnButton2(self, event):
        motor_set_speed(1,2)
        
app = MyApp()
app.MainLoop()
        
