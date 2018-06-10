from operator import itemgetter

class GroupSimulator:
    def __init__(self, groups, matchSimulator):
        self.groups = groups
        self.matchSimulator = matchSimulator

    def simulateAllGroups(self):
        return [self._simulateGroup(g) for g in self.groups]

    def _simulateGroup(self, group):
        print "Simulating Group", group.name
        groupTable = [TableRow(t) for t in group.teams]

        for i in range(len(group.teams)):
            for j in range(i + 1, len(group.teams)):
                teamA = group.teams[i]
                teamB = group.teams[j]
                rowA = groupTable[i]
                rowB = groupTable[j]

                matchResult = self.matchSimulator.simulateMatchWithDraws(teamA, teamB)
                rowA.record(matchResult)
                rowB.record(matchResult)
                print "   {:>13} vs. {:13}:  {:>1} - {:1} ({})".format(teamA.name, teamB.name, matchResult.goalsFor(teamA), matchResult.goalsFor(teamB), matchResult.winnerString())

        # sort by points to find winners
        groupTable.sort(key = lambda x: (x.points, x.goals_for - x.goals_against, x.goals_for, x.team.cost), reverse=True)

        printLine()
        print "    ",
        TableRow.printHeader()
        printLine()
        for i, row in enumerate(groupTable):
            if i == 0:
                result = "(winner)"
            elif i == 1:
                result = "(runner-up)"
            else:
                result = ""
            print "    ",
            row.printRow(result)
        printLine()
        print ""
        return GroupResult(group, groupTable[0].team, groupTable[1].team)

def printLine():
    print "    -------------------------------------------------------------------"

# represents a row in the group table
class TableRow:
    WIN_POINTS = 3
    LOSE_POINTS = 0
    DRAW_POINTS = 1
    DISPLAY_FORMATTER = "| {:>13} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |  {:10}"

    def __init__(self, team, points=0, played=0, win=0, lose=0, draw=0, goals_for=0, goals_against=0):
        self.team = team
        self.points = points
        self.played = played
        self.win = win
        self.lose = lose
        self.draw = draw
        self.goals_for = goals_for
        self.goals_against = goals_against

    def record(self, matchResult):
        self.played += 1
        if matchResult.goalsFor(self.team) == matchResult.goalsAgainst(self.team):
            self.points += TableRow.DRAW_POINTS
            self.draw += 1
        elif matchResult.goalsFor(self.team) > matchResult.goalsAgainst(self.team):
            self.points += TableRow.WIN_POINTS
            self.win += 1
        else:
            self.points += TableRow.LOSE_POINTS
            self.lose += 1
        self.goals_for += matchResult.goalsFor(self.team)
        self.goals_against += matchResult.goalsAgainst(self.team)

    def printRow(self, result):
        print TableRow.DISPLAY_FORMATTER.format(self.team.name, self.points, self.played, self.win, self.lose, self.draw, self.goals_for, self.goals_against, result)

    @staticmethod
    def printHeader():
        star = " " + unichr(9733).encode('utf-8').strip()
        print TableRow.DISPLAY_FORMATTER.format("Team", star, "P", "W", "L", "D", "GF", "GA", "")

class GroupResult:
    def __init__(self, group, winner, runner_up):
        self.group = group
        self.winner = winner
        self.runner_up = runner_up
