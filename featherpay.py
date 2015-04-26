#! /usr/bin/python
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
import subprocess
from panel1 import Panel1
from panel2 import Panel2
from panel3 import Panel3
from panel4 import Panel4



states = ["START", "GETAMOUNT", "QRCODE", "CONFIRM"]

## inherit Frame1 from gui
class MainApp(gui.Frame1):
    def __init__(self, parent):
        gui.Frame1.__init__(self, parent)
        
        self.panels = [Panel1(self), Panel2(self), Panel3(self), Panel4(self)]
        for panel in self.panels:
            panel.Hide()

        self.oldState = 0
        self.ChangeState("START", {})


    def ChangeState(self, newState, params):
        newState = states.index(newState)
        oldPanel = self.panels[self.oldState]
        newPanel = self.panels[newState]
    
        oldPanel.Stop()
 
        newPanel.Start(params)
        self.oldState = newState
            
def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()
    
if __name__ == '__main__':
    main()
          
           
