class KnockoutSimulator:
    def __init__(self, bracket, matchSimulator):
        self.bracket = bracket
        self.matchSimulator = matchSimulator

    def simulateAllStages(self):
        self._simulateStage("Round of 16", self.bracket.round16, self.bracket.quarters)
        self._simulateStage("Quarter-Finals", self.bracket.quarters, self.bracket.semis)
        self._simulateStage("Semi-Finals", self.bracket.semis, self.bracket.finals)
        self.bracket.thirdPlaceMatch[0] = self._findLoser(self.bracket.semis[0], self.bracket.semis[1], self.bracket.finals[0])
        self.bracket.thirdPlaceMatch[1] = self._findLoser(self.bracket.semis[2], self.bracket.semis[3], self.bracket.finals[1])
        self._simulateStage("Third Place", self.bracket.thirdPlaceMatch, self.bracket.third)
        self._simulateStage("Finals", self.bracket.finals, self.bracket.champion)
        self.bracket.runnerUp[0] = self._findLoser(self.bracket.finals[0], self.bracket.finals[1], self.bracket.champion[0])

    def _simulateStage(self, stageName, fromList, nextList):
        print "Simulating Knockout Stage:", stageName
        for i in range(0, len(fromList), 2):
            teamA = fromList[i]
            teamB = fromList[i+1]

            matchResult = self.matchSimulator.simulateMatchWithoutDraws(teamA, teamB)
            if matchResult.goalsFor(teamA) > matchResult.goalsFor(teamB):
                nextList[i/2] = teamA
            else:
                nextList[i/2] = teamB
            print "   {:>13} vs. {:13}:  {:>1} - {:1} ({})".format(teamA.name, teamB.name, matchResult.goalsFor(teamA), matchResult.goalsFor(teamB), matchResult.winnerString())

    def _findLoser(self, teamA, teamB, winner):
        if teamA.name == winner.name:
            return teamB
        return teamA
