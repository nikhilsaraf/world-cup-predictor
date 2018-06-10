#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.team import Team, Stats
from model.group import Group
from model.bracket import Bracket
from predictors.cost import Predictor
from simulators.match import MatchSimulator
from simulators.group import GroupSimulator
from simulators.knockout import KnockoutSimulator
from scoring import ScoringCriteria

def main():
    groups = makeGroups()
    for g in groups:
        print "Group", g.name
        for t in g.teams:
            print "   ", t.name, unichr(163) + str(t.cost)
    print ""

    predictor = Predictor()
    matchSimulator = MatchSimulator(predictor)

    # simulate group
    groupSimulator = GroupSimulator(groups, matchSimulator)
    groupResults = groupSimulator.simulateAllGroups()

    # simulate knockout
    round16 = makeRound16(groupResults)
    bracket = Bracket(round16)
    koSimulator = KnockoutSimulator(bracket, matchSimulator)
    koSimulator.simulateAllStages()

    print ""
    print "Finishing Order:"
    print "Winner:   ", bracket.champion[0].name
    print "Runner Up:", bracket.runnerUp[0].name
    print "Third:    ", bracket.third[0].name
    print ""

    # score teams
    scoringCriteria = ScoringCriteria(Stats(10, 7, 5, 5, 2, 0, 3, -2, 5, 0))
    teams = []
    for g in groups:
        for t in g.teams:
            teamScore = scoringCriteria.teamScore(t)
            teamTuple = (t, teamScore, float(teamScore)/float(t.cost))
            teams.append(teamTuple)
    teams.sort(key=lambda x: (x[2], -x[0].cost), reverse=True)

    # display teams scored by best to worst based on a per-cost basis
    print "Team Scores:"
    printLine()
    pFormat = "|    {:>13} | {:>6} | {:>6} | {:>8} |"
    print pFormat.format("Team", "Score", "Cost", "S/C")
    printLine()
    for tup in teams:
        print pFormat.format(tup[0].name, tup[1], tup[0].cost, "{:.4f}".format(tup[2]))
    printLine()

def printLine():
    print "-------------------------------------------------"

def makeRound16(groupResults):
    round16 = [None] * 16
    for i in range(0, 8, 2):
        round16[i] = groupResults[i].winner
        round16[i + 1] = groupResults[i + 1].runner_up
        round16[i + 8] = groupResults[i + 1].winner
        round16[i + 8 + 1] = groupResults[i].runner_up
    return round16

def makeGroups():
    return [
        Group("A", [
            Team("Egypt", 4),
            Team("Russia", 16),
            Team("Saudi Arabia", 1),
            Team("Uruguay", 20),
        ]),
        Group("B", [
            Team("Iran", 2),
            Team("Morocco", 2),
            Team("Portugal", 31),
            Team("Spain", 70),
        ]),
        Group("C", [
            Team("Australia", 3),
            Team("Denmark", 9),
            Team("France", 80),
            Team("Peru", 5),
        ]),
        Group("D", [
            Team("Argentina", 55),
            Team("Croatia", 20),
            Team("Iceland", 5),
            Team("Nigeria", 5),
        ]),
        Group("E", [
            Team("Brazil", 99),
            Team("Costa Rica", 2),
            Team("Switzerland", 9),
            Team("Serbia", 5),
        ]),
        Group("F", [
            Team("Germany", 99),
            Team("South Korea", 2),
            Team("Mexico", 9),
            Team("Sweden", 7),
        ]),
        Group("G", [
            Team("Belgium", 45),
            Team("England", 33),
            Team("Panama", 1),
            Team("Tunisia", 2),
        ]),
        Group("H", [
            Team("Columbia", 19),
            Team("Japan", 3),
            Team("Poland", 11),
            Team("Senegal", 5),
        ]),
    ]

if __name__ == "__main__":
    main()
