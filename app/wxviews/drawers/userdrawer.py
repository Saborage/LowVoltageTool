from app.wxviews.drawers import *
from app.wxviews.drawers.drawer import Drawer


class UserDrawer(Drawer):
    """Class that will be used to draw users."""
    # Following static variables will be used by every users and will be the same for every single one.
    size = 60 * Drawer.size_hint

    @staticmethod
    def drawUser(pos=(0,0)):
        # Here will be stored more specific data like position and backing user
        pos = pos

    def OnUserUpdate(self, user):
        self.user = user



if __name__ == '__main__':
    pass
