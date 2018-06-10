class ScoringCriteria:
    def __init__(self, stats):
        self.stats = stats

    def teamScore(self, team):
        scoreDict = self.stats.__dict__
        teamDict = team.stats.__dict__

        score = 0
        for k in teamDict:
            score += scoreDict[k] * teamDict[k]
        return score
