import wx
import gui
from wx.lib.pubsub import pub
import pickle

class madFrame(gui.MadFrame):
    def __init__(self, parent):
        gui.MadFrame.__init__(self, parent)
        self.ordre = []
        self.config = []
        self.filename = "config.ini"
        infile = open(self.filename, "rb")
        self.config = pickle.load(infile)
        infile.close()
        self.txtpizza_pris.SetLabelText(self.config[0]+",- kr.")
        self.txtburger_pris.SetLabelText(self.config[1]+",- kr.")
        self.txtcola_pris.SetLabelText(self.config[2]+",- kr.")

    def prisialt(self):
        pris_ialt = self.pizza_choice.GetSelection() * int(self.config[0])
        pris_ialt += self.burger_choise.GetSelection() * int(self.config[1])
        pris_ialt += self.cola_choice.GetSelection() * int(self.config[2])
        return pris_ialt


    def bestil(self, event ):
        self.ordre.append(self.nametxt.GetValue())
        self.ordre.append(self.pizza_choice.GetSelection())
        self.ordre.append(self.burger_choise.GetSelection())
        self.ordre.append(self.cola_choice.GetSelection())
        p = self.prisialt()
        self.ordre.append(p)
        pub.sendMessage("bestilling", varer = self.ordre)
        self.ordre.clear()

    def update( self, event ):
        self.samletpris.SetLabelText(str(self.prisialt())+" ,- kr")


    def slut_mad( self, event ):
        pub.sendMessage("Skjul")
        self.Hide()

class oversigt_mad(gui.Oversigt_mad):
    def __init__(self, parent):
        gui.Oversigt_mad.__init__(self, parent)
        pub.subscribe(self.listner, "bestilling")
        pub.subscribe(self.skjul, "Skjul")
        self.bestilling_list.InsertColumn(0,"Navn")
        self.bestilling_list.InsertColumn(1,"Pizza")
        self.bestilling_list.InsertColumn(2,"Burger")
        self.bestilling_list.InsertColumn(3,"Cola")
        self.bestilling_list.InsertColumn(4,"Pris ialt")
        self.index = 0

    def listner(self, varer):
        print(varer)
        self.bestilling_list.InsertItem(self.index,varer[0])
        self.bestilling_list.SetItem(self.index,1,str(varer[1]))
        self.bestilling_list.SetItem(self.index,2,str(varer[2]))
        self.bestilling_list.SetItem(self.index,3,str(varer[3]))
        self.bestilling_list.SetItem(self.index,4,str(varer[4]))
        self.index += 1

    def skjul(self):
        self.Hide()


class Indstillinger(gui.Indstillinger):
    def __init__(self, parent):
        gui.Indstillinger.__init__(self, parent)
        self.filename = "config.ini"
        self.config = []


    def save( self, event ):
        self.config.append(self.Pizza_pris.GetValue())
        self.config.append(self.Burger_pris.GetValue())
        self.config.append(self.Cola_pris.GetValue())
        outfile = open(self.filename, "wb")
        pickle.dump(self.config, outfile)
        outfile.close()
        self.Hide()

class mainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.madFrame = madFrame(self)
        self.oversigt_mad = oversigt_mad(self)
        self.Indstillinger = Indstillinger(self)

    def close(self, event ):
        exit(0)

    def mad(self, event ):
        self.madFrame.Show()
        self.oversigt_mad.Show()

    def Indstillinger ( self, event ) :
        self.Indstillinger.Show()

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
