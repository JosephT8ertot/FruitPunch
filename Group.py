"""
Creator: Joseph A Tate
Last Edit: 6/25/2021
    Groups class maintains the name, ID, adminUsers, users, players, game teams, memberStats, Leagues, and Tournaments.
"""


# imports
from Player import Player
from User import User
from Team import Team
from Tournament import Tournament
from League import League
from Game import *

# Group class
class Group:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.admins = self.loadAdmins()
        self.members = self.loadMembers()
        self.beerPongTeams = self.loadBPTeams()
        self.snappaTeams = self.loadSnappaTeams()
        self.leagues = self.loadLeagues()
        self.tournaments = self.loadTournaments()
        self.beerPongStats = self.loadBPStats()
        self.snappaStats = self.loadSnappaStats()

    # loads the admin members
    def loadAdmins(self):
        pass  # FIXME returns list

    # loads all the members
    def loadMembers(self):
        pass  # FIXME returns list

    # loads the beer pong teams
    def loadBPTeams(self):
        pass  # FIXME returns list

    # loads the snappa teams
    def loadSnappaTeams(self):
        pass  # FIXME returns list

    # loads the leagues
    def loadLeagues(self):
        pass  # FIXME returns list

    # loads the tournaments
    def loadTournaments(self):
        pass  # FIXME returns list

    # loads the beer pongs stats
    def loadBPStats(self):
        pass  # FIXME returns dict

    # loads the snappa stats
    def loadSnappaStats(self):
        pass  # FIXME returns dict
    # adds member (ONLY IF USER IS ADMIN)

    def addMember(self, member, privilege='normal'):
        if privilege == 'admin' and type(member) == User:
            self.admins.append(member)
        else:
            self.members.append(member)

    # deletes member (ONLY IF DELETER IS ADMIN AND MEMBER NOT)
    def deleteMember(self, member):
        if member not in self.admins:
            self.members.remove(member)
        elif member not in self.members:
            return Exception('No such member exists.')
        else:
            return Exception('Can\'t delete admin.')

    # OTHER METHODS
