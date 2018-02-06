from app.wxviews.items.networkrepr import NetworkRepr
from app.wxviews.patterns.singleton import Singleton
from app.models import *


@Singleton
class Engine:
    def __init__(self):
        self.toolbarClicked = False
        self.network = NetworkRepr()
        self.drawer = None
        self.item = None

    def OnRightClick(self, event):
        if self.toolbarClicked:
            self.toolbarClicked = False
            # Reinitialize drawer state
            self.drawer = None
        event.Skip()

    def releaseFocus(self):
        self.toolbarClicked = False
        self.drawer = None
        self.item = None

    def AddNode(self, node):
        self.network.addNode(node)

    def RemoveNode(self, node):
        self.network.deleteNode(node)

    def UpdateNode(self, node):
        i = self.network.nodes_repr.index(node)
        self.network.updateNode(node, i)

    def AddUser(self, user):
        self.network.addUser(user)

    def RemoveUser(self, user):
        self.network.deleteUser()

    def UpdateUser(self, user):
        i = self.network.users_repr.index(user)
        self.network.updateUser(user, i)

    def AddBranch(self, branch):
        self.AddBranch(branch)

    def DeleteBranch(self, branch):
        self.DeleteBranch(branch)

    def UpdateBranch(self, branch):
        i = self.network.branches_repr.index(branch)
        self.network.updateBranch(branch, i)

if __name__ == '__main__':
    pass
