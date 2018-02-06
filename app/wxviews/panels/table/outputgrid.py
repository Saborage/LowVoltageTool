from app.wxviews.panels.table import *


class OutputGrid:
    """Displays the output of the load flow in a grid"""
    def __init__(self, parent):
        super(OutputGrid, self).__init__()
        Engine.Instance().network.register(self)
        self.grid = wx.grid.Grid(parent=parent, id=wx.ID_ANY, name="Input")
        self.init_GUI()

    def init_GUI(self):
        self.grid.CreateGrid(len(Engine.Instance().network.items), 1)

    def bind_events(self):
        self.grid.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)


if __name__ == '__main__':
    pass
