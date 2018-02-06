import wx
from app.wxviews.core import Engine
from app.wxviews.panels.detailspanelin import DetailsPanelIn
from app.wxviews.panels.detailspanelout import DetailsPanelOut
from app.wxviews.panels.toolbar import ToolBar
from app.wxviews.panels.paintpanel import PaintPanel


class LowVoltageTool(wx.Frame):
    """Main Window"""
    def __init__(self, parent):
        no_resize = wx.DEFAULT_FRAME_STYLE 
        super(LowVoltageTool, self).__init__(parent, title="Low Voltage Tool", style=no_resize)
        # Binding models to GUI
        self.initUI()
        self.Show(True)
        self.Maximize(True)


    def initUI(self):
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\genieelecpsim\\Desktop\\Alexandre Stage 2018\\Logo\\blason-poly.jpg",
                                       wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        # Horizontal box layout
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Vertical box layout
        vbox =  wx.BoxSizer(wx.VERTICAL)
        # Creating Menu bar
        self.menu = wx.MenuBar()
        self.initMenu(self.menu)

        # Main business of the application
        # Creating Panels
        self.mainpanel = wx.Panel(self, wx.ID_ANY)
        self.toolbar = ToolBar(self.mainpanel)
        self.paint_panel = PaintPanel(self.mainpanel)
        self.details_panelIn = DetailsPanelIn(self.mainpanel)
        self.details_panelOut = DetailsPanelOut(self.mainpanel)
        # Adding them to the main one
        # Add(item, size, flags)
        # Proportion lets the Sizer manage the sizes of items according to its value

        vbox.Add(self.details_panelIn, proportion=1, flag=wx.UP | wx.EXPAND)
        vbox.Add(self.details_panelOut, proportion=1, flag=wx.DOWN | wx.EXPAND)

        hbox.Add(self.toolbar, proportion=0.5, flag=wx.LEFT|wx.EXPAND)
        hbox.Add(self.paint_panel, proportion=2.5, flag=wx.CENTER|wx.EXPAND)
        hbox.Add(vbox, proportion=1, flag=wx.RIGHT|wx.EXPAND)

        self.mainpanel.SetSizer(hbox)
        self.mainpanel.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.SetMenuBar(self.menu)

    def OnExitApp(self, event):
        self.Destroy()

    def initMenu(self, menu):
        # Creating a Menu [File]
        file_menu = wx.Menu()
        # Creating an Option [Load]
        load_item = file_menu.Append(wx.ID_FILE, "&Load", "Load a file in Low Voltage Tool")
        # Creating an Option [Save]
        save_item = file_menu.Append(wx.ID_SAVE, "&Save", "Save a file in Low Voltage Tool")
        # Creating an Option [Quit]
        quit_item = file_menu.Append(wx.ID_EXIT, "&Quit", "Leave Low Voltage Tool")
        # Binding the Event_Menu of the Quit_Item Option to the custom OnQuit() method
        menu.Bind(wx.EVT_MENU, self.OnQuit, quit_item)
        menu.Append(file_menu, "&File")
        #Creating a Menu [About]

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    print ("before MainLoop")
    frame = LowVoltageTool(None)
    app.MainLoop()
    print("after MainLoop")
