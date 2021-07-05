"""
Creator: Joseph A Tate
Last Edit: 7/5/2021
    The purpose of this class is to store the Player and User classes, which are used throughout the application to
give the user a involved experience
"""

# imports
from Database import db

# Player class
class Player:
    def __init__(self, email_or_ID):
        self.email_or_ID = email_or_ID
        self.name = None
        self.beerPong = None
        self.snappa = None

    # returns dictionary of stats for player for Beer Pong, returns base dict if player not in database
    def loadBPStats(self):
        self.beerPong = {'shots':0,'sinks':0,'wins':0,'losses':0}
        self.snappa = {'throws':0,'hits':0,'sinks':0,'scores':0,'catches':0,'drops':0,'wins':0,'losses':0}
        self.name = None

    # saves dictionary of stats into player slot in database, creating new slot if player doesn't exist
    def saveStats(self):
        pass  # FIXME add stat save

# User class
class User(Player):
    def __init__(self, email):
        super().__init__(email)
        self.groups = self.groupsLoad()
        self.adminGroups = self.adminGroupsLoad()

    # loads all the groups a user is a part of but does not have access admin privileges to.
    def groupsLoad(self):
        return []
    # loads all the groups a user is a part of and has admin privileges for.
    def adminGroupsLoad(self):
        return []
    # creates a new Group as long as no group in self.adminGroups has same name
    def createGroup(self, name):
        pass
    # leaves group from database and user lists unless user is only admin, then returns Exception('Only Admin')
    def leaveGroup(self):
        pass
    # deletes group from database and user lists, only option if Exception('Only Admin') returned
    def deleteGroup(self):
        pass