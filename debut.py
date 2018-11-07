import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

months = ["march", "april", "may", "june", "july", "august", "september", "october"]
years = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

statLst = []
debuts = []
playerSplit = []
opposingTeamSplit = []
isolate = []
debutStats = []
inningsPitchedSplit = []
earnedRunsSplit = []
hitsSplit = []
mlbDebutData = []

for m in months:

    # specify Baseball Reference URL
    quote_page = 'http://www.espn.com/mlb/debuts/_/month/' + m

    # Call BeautifulSoup web parser

    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    table = soup.find("table", {'class': 'tablehead'})
    rows = table.findAll('tr')
    data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

    for d in data:
        print(d)
        statLine = str(d)
        if "MLB" not in statLine:
            if "DATE" not in statLine:
                if "debuts" not in statLine:
                    statLst = statLine.split("']")

                    # DEBUT DATE
                    debutDate = statLst[0][3:] + "/2018"
                    #

                    playerInfo = statLst[1].__len__()
                    playerName = str(statLst[1][4:(playerInfo - 7)])
                    playerSplit = playerName.split("'")

                    # PLAYER NAME
                    rookieName = playerSplit[0]
                    #

                    # TEAM NAME
                    teamName = statLst[1][playerInfo - 3: playerInfo]
                    #

                    # POSITION
                    position = statLst[2][4:]
                    #

                    if "RP" in position or "SP" in position:

                        # AGE
                        age = statLst[3][4:]
                        #

                        opposingTeamSplit = statLst[4].split(":")
                        isolate = opposingTeamSplit[0].split("'")

                        # OPPOSING TEAM
                        opposingTeam = isolate[1]
                        #

                        debutStats = opposingTeamSplit[1].split(",")
                        inningsPitchedSplit = debutStats[0].split(" ")

                        # INNINGS PITCHED
                        inningsPitched = inningsPitchedSplit[1]
                        #

                        earnedRunsSplit = debutStats[1].split(" ")

                        # EARNED RUNS
                        earnedRuns = earnedRunsSplit[1]
                        #

                        hitsSplit = debutStats[2].split(" ")

                        # HITS
                        hits = hitsSplit[1]
                        #

                        # DECISION
                        if debutStats.__len__() > 3:
                            decision = debutStats[3]
                        else:
                            decision = "ND"

                        mlbDebut = debutDate + "," + rookieName + "," + teamName + "," + position + "," + age + "," + opposingTeam + "," + inningsPitched + "," + earnedRuns + "," + hits + "," + decision
                        mlbDebutData.append(mlbDebut)
                       # print(mlbDebut)

for y in years:
    for m in months:
        quote_page = 'http://www.espn.com/mlb/debuts/_/year/' + str(y) + '/month/' + m

        # Call BeautifulSoup web parser

        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')

        table = soup.find("table", {'class': 'tablehead'})
        rows = table.findAll('tr')
        data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

        for d in data:
            statLine = str(d)
            if "MLB" not in statLine:
                if "DATE" not in statLine:
                    if "debuts" not in statLine:
                        statLst = statLine.split("']")

                        # DEBUT DATE
                        debutDate = statLst[0][3:] + "/" + str(y)
                        #

                        playerInfo = statLst[1].__len__()
                        playerName = str(statLst[1][4:(playerInfo - 7)])
                        playerSplit = playerName.split("'")

                        # PLAYER NAME
                        rookieName = playerSplit[0]
                        #

                        # TEAM NAME
                        teamName = statLst[1][playerInfo - 3: playerInfo]
                        #

                        # POSITION
                        position = statLst[2][4:]
                        #

                        if "RP" in position or "SP" in position:

                            # AGE
                            age = statLst[3][4:]
                            #

                            opposingTeamSplit = statLst[4].split(":")
                            isolate = opposingTeamSplit[0].split("'")

                            # OPPOSING TEAM
                            opposingTeam = isolate[1]
                            #

                            debutStats = opposingTeamSplit[1].split(",")
                            inningsPitchedSplit = debutStats[0].split(" ")

                            # INNINGS PITCHED
                            inningsPitched = inningsPitchedSplit[1]
                            #

                            earnedRunsSplit = debutStats[1].split(" ")

                            # EARNED RUNS
                            earnedRuns = earnedRunsSplit[1]
                            #

                            hitsSplit = debutStats[2].split(" ")

                            # HITS
                            hits = hitsSplit[1]
                            #

                            # DECISION
                            if debutStats.__len__() > 3:
                                decision = debutStats[3]
                            else:
                                decision = "ND"

                            mlbDebut = debutDate + "," + rookieName + "," + teamName + "," + position + "," + age + "," + opposingTeam + "," + inningsPitched + "," + earnedRuns + "," + hits + "," + decision
                            mlbDebutData.append(mlbDebut)
                           # print(mlbDebut)


with open('/Users/AaronKanzer/Desktop/mlbDebutDataFINAL1.csv', 'w') as f:
    writer = csv.writer(f)
    for mlbDebut in mlbDebutData:
        writer.writerow([mlbDebut])

print("done")
