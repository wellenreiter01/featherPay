# -*- coding: utf-8 -*- 

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


###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class Frame1
###########################################################################

class Frame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,320 ), style = 0|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class panel_one
###########################################################################

class panel_one ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 240,320 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.button1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"/home/featherpay/featherPay/images/accept-button-240x320.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.button1.SetMinSize( wx.Size( 240,320 ) )
		
		self.button1.SetMinSize( wx.Size( 240,320 ) )
		
		bSizer2.Add( self.button1, 0, wx.ALL, 0 )
		
		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.button1Func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button1Func( self, event ):
		event.Skip()
	

###########################################################################
## Class panel_two
###########################################################################

class panel_two ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 239,319 ), style = wx.TAB_TRAVERSAL )
		
		gSizer1 = wx.GridSizer( 5, 1, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"FTC Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.ftcvalue = wx.StaticText( self, wx.ID_ANY, u"ftcvalue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ftcvalue.Wrap( -1 )
		self.ftcvalue.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.ftcvalue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Transaction Amount", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.tamount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.tamount.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.tamount, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.button2 = wx.Button( self, wx.ID_ANY, u"Process", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		# Connect Events
		self.button3.Bind( wx.EVT_BUTTON, self.button3Func )
		self.button2.Bind( wx.EVT_BUTTON, self.button2Func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button3Func( self, event ):
		event.Skip()
	
	def button2Func( self, event ):
		event.Skip()
	

###########################################################################
## Class panel_three
###########################################################################

class panel_three ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 239,319 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer3 = wx.GridSizer( 1, 2, 0, 0 )
		
		gSizer3.SetMinSize( wx.Size( 239,-1 ) ) 
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Total FTC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ftctotal = wx.StaticText( self, wx.ID_ANY, u"ftctotal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ftctotal.Wrap( -1 )
		gSizer3.Add( self.ftctotal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.qrimg = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 208,208 ), 0 )
		gSizer4.Add( self.qrimg, 0, wx.ALIGN_CENTER, 5 )
		
		fgSizer1.Add( gSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		gSizer5 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.button6 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.button6, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.button4 = wx.Button( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.button4, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		fgSizer1.Add( gSizer5, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		# Connect Events
		self.button6.Bind( wx.EVT_BUTTON, self.button6Func )
		self.button4.Bind( wx.EVT_BUTTON, self.button4Func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button6Func( self, event ):
		event.Skip()
	
	def button4Func( self, event ):
		event.Skip()
	

###########################################################################
## Class panel_four
###########################################################################

class panel_four ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 239,319 ), style = wx.TAB_TRAVERSAL )
		
		gSizer6 = wx.GridSizer( 6, 1, 0, 0 )
		
		gSizer7 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"FTC Total:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer7.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ftctotal = wx.StaticText( self, wx.ID_ANY, u"ftctotal", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.ftctotal.Wrap( -1 )
		gSizer7.Add( self.ftctotal, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"TXID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer7.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txid = wx.StaticText( self, wx.ID_ANY, u"txid", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.txid.Wrap( -1 )
		gSizer7.Add( self.txid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		gSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Confirms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer6.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.cgauge = wx.Gauge( self, wx.ID_ANY, 6, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.cgauge.SetValue( 2 ) 
		gSizer6.Add( self.cgauge, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.confirm_count = wx.StaticText( self, wx.ID_ANY, u"confirms", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.confirm_count.Wrap( -1 )
		gSizer6.Add( self.confirm_count, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.button5 = wx.Button( self, wx.ID_ANY, u"New Transaction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.button5, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( gSizer6 )
		self.Layout()
		
		# Connect Events
		self.button5.Bind( wx.EVT_BUTTON, self.button5Func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button5Func( self, event ):
		event.Skip()
	

