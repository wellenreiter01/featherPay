import wx
import gui
import ftc
import platform
from utility import OnEraseBackground
import time

## inherit panel_two from gui          
class Panel2(gui.panel_two):
    def __init__(self, parent):
        gui.panel_two.__init__(self, parent)
        self.parent = parent
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM) ##bgimage
        self.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground) ## bgimage

## process button 'Cancel'
    def button3Func( self, event ):
        self.parent.ChangeState("START", {})

## process button 'Process'            
    def button2Func( self, event ):
        self.params['tamount'] = float(self.tamount.GetValue())
        self.parent.ChangeState("QRCODE", self.params)

    def Start(self, params):
        self.params = params
        self.tamount.SetValue("")
        self.tamount.SetFocus()
        self.params['fvalue'] = ftc.toFTC(1)
        self.ftcvalue.SetLabel(str(self.params['fvalue']))
        self.Show()

    def Stop(self):
        self.Hide()
