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
        groupTable.sort(key = lambda x: (x.team.stats.group_points, x.team.stats.goals_for - x.team.stats.goals_against, x.team.stats.goals_for, x.team.cost), reverse=True)

        # add points for progressing from a group
        groupTable[0].team.stats.group_progress = 1
        groupTable[1].team.stats.group_progress = 1

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
    DISPLAY_FORMATTER = "| {:>13} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} | {:10}"

    def __init__(self, team):
        self.team = team

    def record(self, matchResult):
        if matchResult.goalsFor(self.team) == matchResult.goalsAgainst(self.team):
            self.team.stats.group_points += TableRow.DRAW_POINTS
            self.team.stats.draw += 1
        elif matchResult.goalsFor(self.team) > matchResult.goalsAgainst(self.team):
            self.team.stats.group_points += TableRow.WIN_POINTS
            self.team.stats.win += 1
        else:
            self.team.stats.group_points += TableRow.LOSE_POINTS
            self.team.stats.lose += 1
        self.team.stats.goals_for += matchResult.goalsFor(self.team)
        self.team.stats.goals_against += matchResult.goalsAgainst(self.team)

    def printRow(self, result):
        played = self.team.stats.win + self.team.stats.lose + self.team.stats.draw
        print TableRow.DISPLAY_FORMATTER.format(self.team.name, self.team.stats.group_points, played, self.team.stats.win, self.team.stats.lose, self.team.stats.draw, self.team.stats.goals_for, self.team.stats.goals_against, result)

    @staticmethod
    def printHeader():
        star = " " + unichr(9733).encode('utf-8').strip()
        print TableRow.DISPLAY_FORMATTER.format("Team", star, "P", "W", "L", "D", "GF", "GA", "")

class GroupResult:
    def __init__(self, group, winner, runner_up):
        self.group = group
        self.winner = winner
        self.runner_up = runner_up
