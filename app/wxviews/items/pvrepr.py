from app.models.networkuser import NetworkUser


class UserRepr:
    """Contains GUI info and model info for the User"""
    counter = 0

    def __init__(self, pos=(0,0), user: NetworkUser = NetworkUser()):
        self.backingUser = user
        self.id = UserRepr.counter
        UserRepr.counter += 1
        self.name = "User %s" % self.id


if __name__ == '__main__':
    pass
