# picks the teams based on the selection criteria
from copy import deepcopy

class Picker:
    def __init__(self, costLimit, scorePerUnusedCostUnit, maxUnderfundedPoints):
        self.costLimit = costLimit
        self.scorePerUnusedCostUnit = scorePerUnusedCostUnit
        self.maxUnderfundedPoints = maxUnderfundedPoints

    class GroupPick:
        def __init__(self, group, teams):
            self.group = group
            self.teams = teams
            self.picks = [None] * 2

        @staticmethod
        def compute(groupPicks, costLimit, scorePerUnusedCostUnit, maxUnderfundedPoints):
            cost = sum([t.cost for g in groupPicks for t in g.picks])
            if cost > costLimit:
                return None
            score = sum([t.score for g in groupPicks for t in g.picks])
            underfundedScore = min((float(costLimit - cost) * scorePerUnusedCostUnit), maxUnderfundedPoints)
            return (score, underfundedScore, cost)

    def bestPick(self, groups):
        groupPicks = [self.GroupPick(g, g.teams) for g in groups]
        bestGroupPick = self._pickFromGroups(0, 0, groupPicks, 0, 0)
        if bestGroupPick is None:
            raise Exception("could not make a pick within the bounds specified")

        tup = self.GroupPick.compute(bestGroupPick[0], self.costLimit, self.scorePerUnusedCostUnit, self.maxUnderfundedPoints)
        return bestGroupPick[0], tup[0], tup[1], tup[2]

    def _pickFromGroups(self, startIndex, bestScore, groupPicks, score, cost):
        bestGroupPick = None
        g = groupPicks[startIndex]
        for i in range(0, len(g.teams) - 1):
            firstPick = g.teams[i]
            g.picks[0] = firstPick
            for j in range(i + 1, len(g.teams)):
                secondPick = g.teams[j]
                g.picks[1] = secondPick

                newScore = score + firstPick.score + secondPick.score
                newCost = cost + firstPick.cost + secondPick.cost

                # early check
                if newCost > self.costLimit:
                    continue

                # base case (last item)
                if startIndex == len(groupPicks) - 1:
                    underfundedScore = min((float(self.costLimit - newCost) * self.scorePerUnusedCostUnit), self.maxUnderfundedPoints)
                    newTotalScore = newScore + underfundedScore
                    if newTotalScore > bestScore:
                        bestGroupPick = deepcopy(groupPicks)
                        bestScore = newTotalScore
                        #print "    setting bestGroupPick:", [t.name for g in groupPicks for t in g.picks], " | score =", newTotalScore
                    continue

                # recurse
                innerBestGroupPick = self._pickFromGroups(startIndex + 1, bestScore, groupPicks, newScore, newCost)
                if innerBestGroupPick is None:
                    continue
                bestGroupPick = innerBestGroupPick[0]
                bestScore = innerBestGroupPick[1]

        if bestGroupPick is None:
            return None
        return (bestGroupPick, bestScore)
