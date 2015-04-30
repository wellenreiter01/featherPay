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


import gui
import wx
from utility import OnEraseBackground
import subprocess
import qrcode
from PIL import Image
import os
from config import identifier


## inherit panel_three from gui            
class Panel3(gui.panel_three):
    def __init__(self, parent):
        gui.panel_three.__init__(self, parent)
        self.parent = parent
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM) ##bgimage
        self.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground) ## bgimage

## process button 'Confirm'        
    def button4Func( self, event ):
        self.parent.ChangeState("CONFIRM", self.params)
    
## process button 'Cancel'
    def button6Func( self, event ):
        self.parent.ChangeState("START", {}) 

    def Start(self, params):
        self.params = params
        print 'this is the txid ' + self.params['txid']
        print self.params['tamount']
        ## get new payment address
        self.params['paddress'] = self.__newAddress(self.params['txid'])
        ## calculat total FTC to be charged 'ftotal'
        ftotal = round(float(self.params['tamount']/ self.params['fvalue']), 4)
        self.params['ftotal'] = ftotal
        ## create qrcode
        self.__createQRCode(self.params['txid'], self.params['paddress'], ftotal)
        ##resize image for use in process frame
        qrFile = ("/home/featherpay/featherPay/images/qrcodes/%s.png" % self.params['txid'])
        img_org = Image.open(qrFile)
        width_org, height_org = img_org.size
        factor = 0.32
        width = int(width_org * factor)
        height = int(height_org * factor)
        img_anti = img_org.resize((width, height), Image.ANTIALIAS)
        name, ext = os.path.splitext(qrFile)
        new_image_file = "%s%s%s" % (name, '_qr', ext)
        img_anti.save(new_image_file)
        qrImage = wx.Image(new_image_file, wx.BITMAP_TYPE_ANY)
        ## delete the orginal image to save space
        os.remove(qrFile)
        ## pass information forward to panelThree
        self.ftctotal.SetLabel(str(ftotal))
        self.qrimg.SetBitmap(wx.BitmapFromImage (qrImage))

        self.Show()

    def Stop(self):
        self.Hide()

    def __newAddress(self, txid):
        paddress = subprocess.check_output("feathercoind getnewaddress %s" % txid, shell=True)
        paddress = paddress.replace("\n", "")
        print 'Payment Address ' + paddress
        return paddress

    def __createQRCode(self, txid, paddress, ftotal):
        ltxid = identifier + '-' + txid
        qrdata = ("feathercoin:%s?amount=%s&label=%s") % (paddress, ftotal, ltxid)
        print 'this is the qrcode data ' + qrdata,
        qr = qrcode.QRCode(version=10)
        qr.add_data(qrdata)
        qr.make()
        im = qr.make_image()
        im.save("/home/featherpay/featherPay/images/qrcodes/%s.png" % txid)

