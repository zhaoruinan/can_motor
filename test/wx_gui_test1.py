import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))
        panel = wx.Panel(frame, -1)
        self.radio1 = wx.RadioButton(panel,-1,'Radio1',pos=(10,40),style = wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel,-1,'Radio2',pos=(10,80))
        self.radio3 = wx.RadioButton(panel,-1,'Radio3',pos=(10,120))
        self.check  = wx.CheckBox(panel,-1,'CheckBox',pos = (120, 40),size = (150,20))
        self.button1 = wx.Button(panel,-1,'Radio',pos = (120,80))
        self.button2 = wx.Button(panel,-1,'check',pos = (120,120))
        self.Bind(wx.EVT_BUTTON, self.OnButton1,self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2,self.button2)
        frame.Show()
        return True
    def OnButton1(self, event):
        if self.radio1.GetValue():
            self.button1.SetLabel('Radio1')
        elif self.radio2.GetValue():
            self.button1.SetLabel('Radio2')
        else:
            self.button1.SetLabel('Radio3')
    def OnButton2(self, event):
        if self.check.IsChecked():
            self.button2.SetLabel('Checked')
        else:
            self.button2.SetLabel('UnChecke')
app = MyApp()
app.MainLoop()
        


