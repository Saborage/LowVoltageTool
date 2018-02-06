from app.wxviews.panels.table import *
import wx.grid


class InputGrid(GridTableBase):
    """Used to display the Input parameters for launching a load flow"""
    def __init__(self, parent, data):
        super(InputGrid, self).__init__()
        self.data = data
        Engine.Instance().network.register(self)
        self.col_labels = ['ID', 'V']
        self.data_types = [wx.grid.GRID_VALUE_NUMBER,
                           wx.grid.GRID_VALUE_FLOAT
                           ]
        self.init_GUI()
        self.bind_events()

    # Overriding methods from superclass

    def GetNumberRows(self):
        return len(self.data) + 1

    def GetNumberCols(self):
        return len(self.data[0]) + 1

    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except:
            return ''

    def SetValue(self, row, col, value):
        try:
            self.data[row][col] = value
        except IndexError:
            self.data.append([''] * self.GetNumberCols())
            self.SetValue(row, col, value)
            msg = wx.grid.GridTableMessage(self,
                                           wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED,
                                           1)
            self.GetView().ProcessTableMessage(msg)

    def GetColLabelValue(self, col):
        return self.col_labels[col]

    def GetTypeName(self, row, col):
        return self.data_types[row][col]

    def CanGetValueAs(self, row, col, typeName):
        colType = self.data_types[col].split(':')[0]
        if typeName == colType:
            return True
        return False

    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)
    # End Overriding #

    def init_GUI(self):
        self.grid.CreateGrid(len(Engine.Instance().network.items), 2)
        pass

    def bind_events(self):
        self.grid.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)


if __name__ == '__main__':
    pass
