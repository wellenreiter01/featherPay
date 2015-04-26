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

import requests
import json
from subprocess import Popen, PIPE
import wx

def read_txid():
        with open('/home/ftc/featherPay/txid.log', 'r') as f:
            txid = str(f.readline())
            txid = txid.replace("\n", "")
            print 'read_txid ' + txid
        return txid
        
def get_paddress(txid):
    txid = read_txid()
    paddress = subprocess.check_output("feathercoind getaddressesbyaccount %s" % txid, shell=True)
    paddress = paddress.translate(None, '[" ]')
    paddress = paddress.replace("\n", "")
    print 'get_paddress ' + paddress
    return paddress
    
## add a picture to the background of the frame
def OnEraseBackground(evt):
    dc = evt.GetDC()
     
    if not dc:
        dc = wx.ClientDC(self)
        rect = self.GetUpdateRegion().GetBox()
        dc.SetClippingRect(rect)
    dc.Clear()
    bmp = wx.Bitmap("/home/ftc/featherPay/images/background.jpg")
    dc.DrawBitmap(bmp, 0, 0)            

##check number of confirms for 'paddress' 
def pConfirms(txid):
    txid = read_txid()
    command = "feathercoind listtransactions %s" % txid;
    p = Popen(command, shell = True, stdin = PIPE, stdout = PIPE,
    close_fds = True);
    output = json.load(p.stdout);
    confirms = output[0]['confirmations'];
    return confirms

def get_balance():
    command = "feathercoind getinfo";
    p = Popen(command, shell = True, stdin = PIPE, stdout = PIPE,
    close_fds = True);
    output = json.load(p.stdout);
    balance = output['balance'];
    return balance
        

