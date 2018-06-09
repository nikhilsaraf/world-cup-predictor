class Group:
    # name is A/B/C/etc.
    # teams is array
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

    def __repr__(self):
        return "Group({}, teams={})".format(self.name, self.teams)
