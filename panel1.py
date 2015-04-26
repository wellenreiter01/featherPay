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
        with open('/home/ftc/featherPay/txid.log','r+') as f:
            txid = str(int(f.read().strip())+1)
            f.seek(0)
            f.write(txid)
            f.close()
            print 'create_txid ' + txid
        return txid

