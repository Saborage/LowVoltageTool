import wx
import wx.lib.colourdb
from app.wxviews.panels import *
from wx.lib.floatcanvas import FloatCanvas
from app.wxviews.items.noderepr import NodeRepr
from app.wxviews.drawers.nodedrawer import NodeDrawer
from app.wxviews.items.userrepr import UserRepr
from app.wxviews.drawers.userdrawer import UserDrawer


class PaintPanel(wx.Panel):
    """Canvas to let people draw networks"""
    def __init__(self, parent):
        super(PaintPanel, self).__init__(parent=parent)
        self.network = Engine.Instance().network
        szr = wx.BoxSizer()
        self.canvas = FloatCanvas.FloatCanvas(parent=self)
        szr.Add(self.canvas, proportion=1, flag=wx.EXPAND)
        self.SetSizer(szr)

        #self.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)
        #self.canvas.Bind(wx.EVT_RIGHT_UP, Engine.Instance().OnRightClick)

        # The following is called a lambda expression:
        # It allows us to define functions on-the-go.
        # It is no more than a function without definition.
        self.canvas.Bind(wx.EVT_LEFT_UP, lambda event, panel=self.canvas: self.OnLeftClick(event))
        self.canvas.Bind(wx.EVT_ERASE_BACKGROUND,self.OnWindowBack)

    def OnPaint(self, event):
        dc = wx.PaintDC(self.Update())

    def OnWindowBack(self, event):
        dc = wx.ClientDC(self.canvas)
        rect = self.GetUpdateRegion().GetBox()
        dc.SetClippingRegion(rect)
        print("Panel stay")


    def OnLeftClick(self, event):
        if Engine.Instance().toolbarClicked:
            dc = wx.ClientDC(self.canvas)
            #Add a NODE
            if Engine.Instance().item == "Node":
                x, y = event.GetX(), event.GetY()
                frontNode = NodeRepr()
                frontNode.circle = FC.Circle(XY=(x, y), Diameter=NodeDrawer.size)
                dc.DrawCircle(frontNode.circle.XY[0], frontNode.circle.XY[1], NodeDrawer.size/2)
                Engine.Instance().releaseFocus()
                Engine.Instance().AddNode(frontNode)
            #Add a User
            if Engine.Instance().item == "User":
                x, y = event.GetX(), event.GetY()
                frontUser = UserRepr()
                frontUser.rectangle = FC.Rectangle(XY=(x, y),WH=(10,10), FillColor='Blue')
                dc.DrawRectangle(frontUser.rectangle.XY[0],
                                 frontUser.rectangle.XY[1],
                                 frontUser.rectangle.WH[0],
                                 frontUser.rectangle.WH[1])
                Engine.Instance().releaseFocus()
                #Engine.Instance().AddUser(frontUser)
            if Engine.Instance().item == "Branch":
                x, y = event.GetX(), event.GetY()

if __name__ == '__main__':
    pass
