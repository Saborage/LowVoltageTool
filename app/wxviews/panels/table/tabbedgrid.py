from app.wxviews.panels.table import *


class TabbedGrid:
    """Wraps the two grids showing the information of the elements in the network"""
    def __init__(self, parent):
        super(TabbedGrid, self).__init__()
        # Register as an observer of Top level network
        Engine.Instance().network.register(self)
        self.parent = parent
        self.notebook = wx.Notebook(parent, id=wx.ID_ANY)
        # Initialize Tabs
        # self.tab1 = Inputrid(self.notebook, Engine.Instance().network)
        # self.tab2 = OutputGrid(self.notebook)

        self.tab1 = wx.ListCtrl(self.notebook, id=wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.tab1.Show(True)

        self.tab1.InsertColumn(0, "ID")

        for item in Engine.Instance().network.items:
            self.tab1.InsertItem(0, item.id)

        self.init_GUI()
        self.bind_events()

    def init_GUI(self):
        for item in Engine.Instance().network.items:
            self.tab1.Append(item)
        # Add Tabs to the Tabbed Panel
        #self.notebook.AddPage(self.tab1, "Input")
        #self.notebook.AddPage(self.tab2.grid, "Output")

    def bind_events(self):
        # Binding events
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.notebook.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.notebook.GetSelection()
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.notebook.GetSelection()
        event.Skip()

    def update(self, *args, **kwargs):
        self.network = Engine.Instance().network
        self.tab1.InsertItem(0, Engine.Instance().network.items[-1].id)
        self.tab1.Update()
        # self.tab1.grid.CreateGrid(len(cells), 5)
        # self.tab1.grid.SetCellValue(0, 0, cells[0].name)
        # Update, Add, Fill cells here

    def GetValue(self, row, col):
        return str(self.network.item[row][col])


if __name__ == '__main__':
    pass
