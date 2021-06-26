"""
Creator: Joseph A Tate
Last Edit: 6/25/2021
    no comments yet
"""

# imports
from random import shuffle
from Game import SnappaGame, BeerPongGame
from Team import Team

# League class
class League:
    def __init__(self, name, ID, gamesPerTeam, gameClass):
        self.name = name
        self.ID = ID
        self.gamesPerTeam = gamesPerTeam
        self.gameClass = gameClass
        self.teams = self.loadTeams()
        self.games = self.loadGames()

    # loads the teams
    def loadTeams(self):
        return []

    # adds teams
    def addTeams(self, teams):
        for team in teams:
            self.teams.append(team)

    # deletes team from league
    def deleteTeam(self, team):
        if team in self.teams:
            self.teams.remove(team)
        else:
            return Exception('No such team exists.')

    # loads the Games for league
    def loadGames(self):
        return []

    # creates games for league using self.teams
    def createGames(self):  # FIXME only works with even num of teams
        randTeams = self.teams
        shuffle(randTeams)
        games = []
        for i in range(1, self.gamesPerTeam):
            for j in range(0, len(self.teams) // 2, i):
                teams = (randTeams[2*j], randTeams[2*j+i])
                gameName = "%s vs. %s" % (teams[0].name, teams[1].name)
                gameID = None  # FIXME add ID getter
                game = self.gameClass(gameName, gameID, teams=teams)
                games.append(game)
        self.games = games

# Snappa League
class SnappaLeague(League):
    def __init__(self, name, ID, gamesPerTeam):
        super().__init__(name, ID, gamesPerTeam, SnappaGame)
        self.stats = self.loadStats()

    # loads all snappa league stats
    def loadStats(self):
        return {'throws': 0, 'hits': 0, 'sinks': 0, 'scores': 0, 'catches': 0, 'drops': 0, 'wins': 0, 'losses': 0}

    # saves the snappa league stats
    def saveStats(self):
        pass

# BeerPong League class
class BeerPongLeague(League):
    def __init__(self, name, ID, gamesPerTeam):
        super().__init__(name, ID, gamesPerTeam, BeerPongGame)
        self.stats = self.loadStats()

    # loads the beerPong league stats
    def loadStats(self):
        return {'shots':0,'sinks':0,'wins':0,'losses':0}

    # saves the beer pong league stats
    def saveStats(self):
        pass