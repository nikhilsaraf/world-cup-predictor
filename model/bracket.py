class Bracket:
    def __init__(self, round16):
        self.round16 = round16
        self.quarters = [None] * 8
        self.semis = [None] * 4
        self.finals = [None] * 2
        self.thirdPlaceMatch = [None] * 2
        # results
        self.champion = [None] * 1
        self.runnerUp = [None] * 1
        self.third = [None] * 1
