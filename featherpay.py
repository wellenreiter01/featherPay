#! /usr/bin/python

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
          
           
