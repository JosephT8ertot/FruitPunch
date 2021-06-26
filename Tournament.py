"""
Creator: Joseph A Tate
Last Edit: 6/25/2021
    no comments yet
"""


# imports
from random import random
from Game import SnappaGame, BeerPongGame

# SnappaTournament class
class Tournament:

    def __init__(self, name, ID, gameClass):
        self.name = name
        self.ID = ID
        self.gameClass = gameClass
        self.teams = self.loadTeams()
        self.games = self.loadGames()

    # loads the Teams
    def loadTeams(self):
        pass

    # adds teams to tournament
    def addTeams(self, teams):
        for team in teams:
            self.teams.append(team)

    # deletes a team from the tournament.
    def deleteTeam(self, team):
        if team in self.teams:
            self.teams.remove(team)
        else:
            return Exception('No such team exists.')

    # loads the Games
    def loadGames(self):
        pass  # FIXME returns a list of Nodes with games

    # creates a list of Game Nodes using self.teams
    def createGames(self):
        if len(self.teams) % 2 == 0:
            if len(self.teams) != 0:
                teams = random.shuffle(self.teams)
                teams = zip(teams[0::2]), teams[0::2]
                games = []
                for i in range(len(teams)):
                    gameName = "%s vs. %s" % (teams[i][0].name, teams[i][1].name)
                    gameID = None  # FIXME add gameID getter
                    games.append(self.GameType(gameName, gameID, teams[i]))
            return Exception('No teams available.')
        return Exception('Odd number of teams.')

class SnappaTournament(Tournament):
    def __init__(self, name, ID):
        super().__init__(self, name, ID, SnappaGame)
        self.stats = self.loadStats()

    # loads the snappa stats
    def loadStats(self):
        return {'throws':0,'hits':0,'sinks':0,'scores':0,'catches':0,'drops':0,'wins':0,'losses':0}

    # saves the snappa tournament stats
    def saveStats(self):
        pass

class BeerPongTournament(Tournament):
    def __init__(self, name, ID):
        super().__init__(self, name, ID, BeerPongGame)
        self.stats = self.loadStats()

    # loads the beer pong stats
    def loadStats(self):
        return {'shots':0,'sinks':0,'wins':0,'losses':0}

    # saves the beer pong tournament stats
    def saveStats(self):
        pass