import gui
import wx
from utility import OnEraseBackground
import utility
import datetime
import os
import config
import time
import threading


class Panel4(gui.panel_four):
    def __init__(self, parent):
        gui.panel_four.__init__(self, parent)
        self.parent = parent
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM) ##bgimage
        self.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground) ## bgimage
        self.cgauge.SetRange (6)
                
    def confirmTimer(self):
        self.timer = wx.CallLater
        txid = utility.read_txid()
        confirms = utility.pConfirms(self.params['paddress'])
        self.confirms = confirms
    
        if confirms < 6:
            print "the timer has started"
            self.timer = wx.CallLater(10000, self.confirmTimer) #increase to 10000 after testing
            
        print "confirmTimer called"
        self.confirm_count.SetLabel(str(confirms))
        self.cgauge.SetValue(int(confirms))
                
## process button 'New Transaction'
    def button5Func( self, event ):
        self.parent.ChangeState("START", {})
        
    def Start(self, params):
        self.params = params
        ## at this point we assume the transaction is complete so we log it
        self.__txLog(self.params['txid'], self.params['fvalue'], self.params['tamount'], self.params['ftotal'])
        ## set some values on the panel
        self.ftctotal.SetLabel(str(self.params['ftotal']))
        self.txid.SetLabel(str(self.params['txid']))
        ## sort out the panel display
        self.Show()
        self.confirmTimer()
        
    def Stop(self):
        if self.confirms < 6:
            self.timer.Stop()
            self.Hide()
        
    def __txLog(self, txid, fvalue, tamount, ftotal):
        txtime = datetime.datetime.now()
        ltxid = config.identifier + '-' + txid

        writeHeader = (False == os.path.exists(config.logfile))

        f = open(config.logfile, 'a+')

        if writeHeader:
            f.write("transaction-id,txtime,ftc-value,transaction-amount,ftc-total\n")

        f.write(ltxid + ',' + str(txtime) + ',' + str(fvalue) + ',' + str(tamount) + ',' + str(ftotal) + '\n')
        f.close()

