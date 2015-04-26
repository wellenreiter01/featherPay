# This file is part of featherPay.
# Copyright (c) 2015 Rob Toft
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
#to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import wx
import gui
from utility import get_value
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
        self.params['fvalue'] = get_value()
        self.ftcvalue.SetLabel(str(self.params['fvalue']))
        self.Show()

    def Stop(self):
        self.Hide()
