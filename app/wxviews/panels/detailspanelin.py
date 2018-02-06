from app.wxviews.panels.table.tabbedgrid import TabbedGrid
from app.wxviews.panels import *


class DetailsPanelIn(wx.Panel):
    """Show network elements and their values"""
    def __init__(self, parent):
        super(DetailsPanelIn, self).__init__(parent=parent)
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.initGUI()

    def initGUI(self):
        # Vertical Box Layout
        # Tabbed Panel
        notebook = TabbedGrid(self)
        # Add the button to launch the load flow
        validate_btn = wx.Button(self, id=wx.ID_ANY, label="Validate Value")
        # set layouts
        low_szr = wx.BoxSizer(orient=wx.HORIZONTAL)
        low_szr.Add(validate_btn, 1, flag=wx.EXPAND)
        self.sizer.Add(notebook.notebook, proportion=4.5, flag=wx.TOP|wx.EXPAND)
        self.sizer.Add(low_szr, proportion=0.5, flag=wx.BOTTOM)
        self.SetSizerAndFit(self.sizer)

        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)


if __name__ == '__main__':
    pass
