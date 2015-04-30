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
from utility import OnEraseBackground


## inherit panel_one from gui        
class Panel1(gui.panel_one):
    def __init__(self, parent):
        gui.panel_one.__init__(self, parent)
        self.parent = parent
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM) ##bgimage
        self.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground) ## bgimage
        
## process button 'FTC Accepted Here'
    def button1Func( self, event ):
        params = {}
        params['txid'] = self.__get_txid();
        self.parent.ChangeState("GETAMOUNT", params)

    def Start(self, params):
        self.Show()

    def Stop(self):
        self.Hide()

    def __get_txid(self):
        with open('/home/featherpay/featherPay/txid.log','r+') as f:
            txid = str(int(f.read().strip())+1)
            f.seek(0)
            f.write(txid)
            f.close()
            print 'create_txid ' + txid
        return txid

