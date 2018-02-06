from app.wxviews.panels import *
from app.wxviews.drawers.nodedrawer import NodeDrawer
from app.wxviews.drawers.userdrawer import UserDrawer


class ToolBar(wx.Panel):
    """Tool Bar with buttons for drawing"""
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent=parent)
        layout = wx.GridSizer(rows=5, cols=1, gap=(parent.GetSize()[0]/50, parent.GetSize()[1]/50))
        # Node, Branch, Bracket, User, PV
        self.node_btn = wx.Button(self, id=wx.ID_ANY, label="Node", name="node")
        self.branch_btn = wx.Button(self, id=wx.ID_ANY, label="Branch", name="branch")
        self.user_btn = wx.Button(self, id=wx.ID_ANY, label="User", name="user")
        self.pv_btn = wx.Button(self, id=wx.ID_ANY, label="PV", name="pv")
        self.eraser_btn = wx.Button(self, id=wx.ID_ANY, label="Eraser", name="eraser")

        self.bindEvents()

        self.add = layout.Add(self.node_btn, flag=wx.EXPAND)
        layout.Add(self.branch_btn, flag=wx.EXPAND)
        layout.Add(self.user_btn, flag=wx.EXPAND)
        layout.Add(self.pv_btn, flag=wx.EXPAND)
        layout.Add(self.eraser_btn, flag=wx.EXPAND)

        self.SetSizer(layout)
        self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def bindEvents(self):
        # Event binding
        self.node_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.node_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.branch_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.branch_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.user_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.user_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.pv_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.pv_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        self.eraser_btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.eraser_btn.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

    def OnButtonClicked(self, event):
        source = event.GetEventObject()
        if not Engine.Instance().toolbarClicked:
            Engine.Instance().toolbarClicked = True
            if source.GetName() == "node":
                # Initialize Drawer state
                Engine.Instance().drawer = NodeDrawer()
                Engine.Instance().item = "Node"
            elif source.GetName() == "branch":
                # Initialize Drawer state
                pass
            elif source.GetName() == "user":
                # Initialize Drawer state
                Engine.Instance().drawer = UserDrawer()
                Engine.Instance().item = "User"
            elif source.GetName() == "pv":
                # Initialize Drawer state
                pass
            else:
                # Initialize Drawer state
                pass
        event.Skip()


if __name__ == '__main__':
    pass
