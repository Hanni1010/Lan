# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LANparty Administration", pos = wx.DefaultPosition, size = wx.Size( 585,387 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )
		
		self.m_menubar2.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Mad", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem4 )
		
		self.m_menuitem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Indstillinger", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuitem6 )
		
		self.m_menubar2.Append( self.m_menu2, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Bestil mad", wx.Point( -1,-1 ), wx.DefaultSize, wx.BORDER_NONE )
		self.m_button3.SetFont( wx.Font( 150, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_button3.SetBackgroundColour( wx.Colour( 255, 59, 215 ) )
		
		bSizer2.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.close, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.mad, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.Indstillinger, id = self.m_menuitem6.GetId() )
		self.m_button3.Bind( wx.EVT_BUTTON, self.mad )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()
	
	def mad( self, event ):
		event.Skip()
	
	def Indstillinger( self, event ):
		event.Skip()
	
	

###########################################################################
## Class MadFrame
###########################################################################

class MadFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bestilling", pos = wx.Point( 100,100 ), size = wx.Size( 500,289 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.nametxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.nametxt.SetToolTip( u"Navn" )
		self.nametxt.SetHelpText( u"Navn" )
		
		bSizer3.Add( self.nametxt, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Pizza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txtpizza_pris = wx.StaticText( self, wx.ID_ANY, u"45,- kr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtpizza_pris.Wrap( -1 )
		
		gSizer1.Add( self.txtpizza_pris, 0, wx.ALL, 5 )
		
		pizza_choiceChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.pizza_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pizza_choiceChoices, 0 )
		self.pizza_choice.SetSelection( 0 )
		gSizer1.Add( self.pizza_choice, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Burger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txtburger_pris = wx.StaticText( self, wx.ID_ANY, u"45,- kr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtburger_pris.Wrap( -1 )
		
		gSizer1.Add( self.txtburger_pris, 0, wx.ALL, 5 )
		
		burger_choiseChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.burger_choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, burger_choiseChoices, 0 )
		self.burger_choise.SetSelection( 0 )
		gSizer1.Add( self.burger_choise, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Cola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		
		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txtcola_pris = wx.StaticText( self, wx.ID_ANY, u"12,- kr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtcola_pris.Wrap( -1 )
		
		gSizer1.Add( self.txtcola_pris, 0, wx.ALL, 5 )
		
		cola_choiceChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.cola_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cola_choiceChoices, 0 )
		self.cola_choice.SetSelection( 0 )
		gSizer1.Add( self.cola_choice, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Samlet pris:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.samletpris = wx.StaticText( self, wx.ID_ANY, u"ialt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.samletpris.Wrap( -1 )
		
		self.samletpris.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer1.Add( self.samletpris, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Bestil", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Afslut", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.pizza_choice.Bind( wx.EVT_CHOICE, self.update )
		self.burger_choise.Bind( wx.EVT_CHOICE, self.update )
		self.cola_choice.Bind( wx.EVT_CHOICE, self.update )
		self.m_button1.Bind( wx.EVT_BUTTON, self.bestil )
		self.m_button2.Bind( wx.EVT_BUTTON, self.slut_mad )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def update( self, event ):
		event.Skip()
	
	
	
	def bestil( self, event ):
		event.Skip()
	
	def slut_mad( self, event ):
		event.Skip()
	

###########################################################################
## Class Oversigt_mad
###########################################################################

class Oversigt_mad ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Oversigt over madbestillinger", pos = wx.Point( 800,100 ), size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.bestilling_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer4.Add( self.bestilling_list, 1, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Indstillinger
###########################################################################

class Indstillinger ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Indstillinger", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"Lol" )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.Priser = wx.StaticText( self, wx.ID_ANY, u"Priser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Priser.Wrap( -1 )
		
		self.Priser.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		bSizer4.Add( self.Priser, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Pizza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		
		gSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.Pizza_pris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Pizza_pris, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Burger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		
		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.Burger_pris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Burger_pris, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Cola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		
		gSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.Cola_pris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Cola_pris, 0, wx.ALL, 5 )
		
		self.Gem = wx.Button( self, wx.ID_ANY, u"Gem", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Gem.SetLabelMarkup( u"Gem" )
		self.Gem.SetDefault()
		gSizer2.Add( self.Gem, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Gem.Bind( wx.EVT_BUTTON, self.save )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def save( self, event ):
		event.Skip()
	

