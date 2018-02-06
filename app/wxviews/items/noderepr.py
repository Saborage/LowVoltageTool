from app.models.networknode import NetworkNode


class NodeRepr:
    """Contains GUI info and model info for the Node"""
    counter = 0

    def __init__(self, pos=(0,0), diameter=0, node: NetworkNode = NetworkNode(), circle=None):
        self.backingNode = node
        self.id = NodeRepr.counter
        self.circle = circle
        NodeRepr.counter += 1
        self.name = "Node %s" % self.id


if __name__ == '__main__':
    pass
