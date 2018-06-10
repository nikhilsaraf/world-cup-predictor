class Team:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return "Team({}, cost={})".format(self.name, self.cost)
