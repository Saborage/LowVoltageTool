from app.wxviews.drawers.drawer import Drawer


class PvDrawer(Drawer):
    """Class that will be used to draw users."""
    # Following static variables will be used by every users and will be the same for every single one.
    size = 60 * Drawer.size_hint

    @staticmethod
    def drawPv(pos=(0,0)):
        # Here will be stored more specific data like position and backing user
        pos = pos

    def OnPvUpdate(self, pv):
        self.user = user



if __name__ == '__main__':
    pass
