class Team:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.stats = Stats()

    def __repr__(self):
        return "Team({}, cost={})".format(self.name, self.cost)

class Stats:
    def __init__(self):
        self.champions = 0
        self.runner_up = 0
        self.third = 0
        self.group_progress = 0
        self.group_points = 0
        self.win = 0
        self.draw = 0
        self.lose = 0
        self.goals_for = 0
        self.goals_against = 0
