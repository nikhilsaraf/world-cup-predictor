class Team:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.stats = Stats()
        self.score = 0

    def __repr__(self):
        return "Team({}, cost={})".format(self.name, self.cost)

class Stats:
    def __init__(self, champions=0, runner_up=0, third=0, win=0, draw=0, lose=0, goals_for=0, goals_against=0, group_progress=0, group_points=0):
        self.champions = champions
        self.runner_up = runner_up
        self.third = third
        self.win = win
        self.draw = draw
        self.lose = lose
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.group_progress = group_progress
        self.group_points = group_points
