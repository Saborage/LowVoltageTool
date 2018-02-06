from app.wxviews.drawers import *
from app.wxviews.drawers.drawer import Drawer


class NodeDrawer(Drawer):
    """Class that will be used to draw nodes."""
    # Following static variables will be used by every nodes and will be the same for every single one.
    size = 10 * Drawer.size_hint

    @staticmethod
    def drawNode(pos=(0,0)):
        # Here will be stored more specific data like position and backing node
        pos = pos

    def OnNodeUpdate(self, node):
        self.node = node


if __name__ == '__main__':
    pass
