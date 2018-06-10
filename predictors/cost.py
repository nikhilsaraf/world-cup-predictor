# cost-based predictor

class Predictor:
    def __init__(self):
        pass

    def predictGoals(self, teamA, teamB):
        a = float(teamA.cost)
        b = float(teamB.cost)

        pNotDraw = float(abs(a - b)) / (a + b)
        pDraw = 1.0 - pNotDraw
        if pDraw >= 0.55:
            if (a + b) >= 80:
                return (3, 3)
            elif (a + b) >= 50:
                return (2, 2)
            elif (a + b) >= 16:
                return (1, 1)
            else:
                return (0, 0)

        pWinA = a / (a + b)
        goalsA = self._goalsForProbability(pWinA, (a + b))
        if goalsA:
            return goalsA

        pWinB = b / (a + b)
        goalsB = self._goalsForProbability(pWinB, (a + b))
        if goalsB:
            # invert because B was the winner here
            return (goalsB[1], goalsB[0])

        if pWinA > pWinB:
            return (1, 0)
        elif pWinA < pWinB:
            return (0, 1)
        raise Exception("unable to predict for teams: " + str([teamA, teamB]))

    def _goalsForProbability(self, pWin, sumCost):
        if pWin >= 0.7:
            if sumCost >= 90:
                return (4, 0)
            elif sumCost >= 70:
                return (3, 1)
            elif sumCost >= 50:
                return (3, 0)
            elif sumCost >= 30:
                return (2, 1)
            elif sumCost >= 15:
                return (2, 0)
            else:
                return (1, 0)

        if pWin >= 0.5:
            if sumCost >= 80:
                return (4, 2)
            elif sumCost >= 50:
                return (3, 2)
            elif sumCost >= 30:
                return (2, 1)
            else:
                return (1, 0)

        return None
        
