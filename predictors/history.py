# history-based predictor
import requests
import re

class Predictor:
    def __init__(self):
        self.baseURL = "https://raw.githubusercontent.com/openfootball/world-cup/master/"
        self.folders = [
#            "1930--uruguay",
#            "1934--italy",
#            "1938--france",
#            "1950--brazil",
#            "1954--switzerland",
#            "1958--sweden",
#            "1962--chile",
#            "1966--england",
#            "1970--mexico",
#            "1974--west-germany",
#            "1978--argentina",
#            "1982--spain",
#            "1986--mexico",
#            "1990--italy",
            "1994--united-states",
            "1998--france",
            "2002--south-korea-n-japan",
            "2006--germany",
            "2010--south-africa",
            "2014--brazil"
        ]
        self.filenames = ["/cup.txt", "/cup_finals.txt"]
        self.data = {}
        self.learn()

    class DataPoint:
        def __init__(self, teamA, teamB, goalsA, goalsB):
            self.teamA = teamA
            self.teamB = teamB
            self.goalsA = goalsA
            self.goalsB = goalsB
        
        def __repr__(self):
            return "DataPoint({} {}-{} {})".format(self.teamA, self.goalsA, self.goalsB, self.teamB)

    def learn(self):
        self.data = {}
        for folder in self.folders:
            for filename in self.filenames:
                url = self.baseURL + folder + filename
                r = requests.get(url, allow_redirects=True)
                for line in r:
                    line = re.sub('\([0-9]+-[0-9]+\)', '', line)
                    line = re.sub('a.e.t. \([0-9]-[0-9], [0-9]-[0-9]\)', '', line)
                    line = re.sub('[0-9]+-[0-9]+[a-z][A-Z]', '', line)
                    line = re.sub('May|June|July|August', '', line)
                    line = re.sub('(pen|a.e.t.|aet)\s+[0-9]-[0-9]', '', line)
                    line = re.sub('West Germany', 'Germany', line)
                    line = re.sub('Soviet Union', 'Russia', line)
                    searchObj = re.search(r'[0-9]+\s+\b([A-Za-z\s]+)([0-9]+)-([0-9]+)(.+)@', line)
                    if not searchObj:
                        continue

                    teamA = searchObj.group(1).strip()
                    goalsA = int(searchObj.group(2))
                    goalsB = int(searchObj.group(3))
                    teamB = searchObj.group(4).strip()

                    v1 = self.data.get(teamA)
                    if not v1:
                        v1 = []
                        self.data[teamA] = v1
                    v1.append(self.DataPoint(teamA, teamB, goalsA, goalsB))

                    v2 = self.data.get(teamB)
                    if not v2:
                        v2 = []
                        self.data[teamB] = v2
                    v2.append(self.DataPoint(teamB, teamA, goalsB, goalsA))
         
    #    for k in self.data:
    #        print k
    #        for d in self.data[k]:
    #            print "    ", d

    def predictGoals(self, teamA, teamB):
        if teamA.name not in self.data and teamB.name not in self.data:
            return (0, 0)
        elif teamA.name not in self.data:
            return (0, 2)
        elif teamB.name not in self.data:
            return (2, 0)

        points = self.data[teamA.name]
        relevant = [d for d in points if d.teamB == teamB.name]
        if len(relevant) == 0:
            # they never played each other
            return (1, 1)

        goalsA = sum([d.goalsA for d in relevant])/len(relevant)
        goalsB = sum([d.goalsB for d in relevant])/len(relevant)
        return (goalsA, goalsB)

    # make teamB always win for now
    def predictPenaltiesWinner(self, teamA, teamB):
        return teamB
