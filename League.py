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
from User import User


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
    def createGames(self):  # FIXME may have repeats, make better
        games = []
        randTeams = self.teams
        for i in range(self.gamesPerTeam):
            shuffle(randTeams)
            for j in range(len(randTeams) // 2):
                teams = [randTeams[i + j], randTeams[(i + j + len(self.teams) // 2) % len(randTeams)]]
                gameName = ""
                gameID = 123
                games.append(self.gameClass(gameName, gameID, teams))
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