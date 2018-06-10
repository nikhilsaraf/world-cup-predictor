class MatchSimulator:
    def __init__(self, predictor):
        self.predictor = predictor

    def simulateMatchWithDraws(self, teamA, teamB):
        goals = self.predictor.predictGoals(teamA, teamB)
        return MatchResult(teamA, teamB, goals[0], goals[1])

    def simulateMatchWithoutDraws(self, teamA, teamB):
        goals = self.predictor.predictGoals(teamA, teamB)
        if goals[0] != goals[1]:
            return MatchResult(teamA, teamB, goals[0], goals[1])

        penaltiesWinner = self.predictor.predictPenaltiesWinner(teamA, teamB)
        if penaltiesWinner.name == teamA.name:
            return MatchResult(teamA, teamB, goals[0] + 1, goals[1])
        elif penaltiesWinner.name == teamB.name:
            return MatchResult(teamA, teamB, goals[0], goals[1] + 1)
        else:
            raise Exception("error predicting penalties winner")

class MatchResult:
    def __init__(self, teamA, teamB, goalsA, goalsB):
        self.teamA = teamA
        self.teamB = teamB
        self.goalsA = goalsA
        self.goalsB = goalsB

    def goalsFor(self, team):
        if self.teamA == team:
            return self.goalsA
        elif self.teamB == team:
            return self.goalsB
        else:
            raise Exception("Invalid team passed in: " + team)
        
    def goalsAgainst(self, team):
        if self.teamA == team:
            return self.goalsB
        elif self.teamB == team:
            return self.goalsA
        else:
            raise Exception("Invalid team passed in: " + team)

    def winnerString(self):
        if self.goalsA == self.goalsB:
            return "DRAW"
        elif self.goalsA > self.goalsB:
            return self.teamA.name
        return self.teamB.name
