#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.team import Team
from model.group import Group

def main():
    groups = makeGroups()
    for g in groups:
        print "Group", g.name
        for t in g.teams:
            print "   ", t.name, unichr(163) + str(t.cost)

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
