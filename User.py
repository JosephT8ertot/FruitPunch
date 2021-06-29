"""
Creator: Joseph A Tate
Last Edit: 6/25/2021
    The User class is a child class to Player, where they have stats, a name, and ID. However, a user also has access
to login to the system, create groups, interact with groups, create users and pull up various statistics.
"""


# imports
from Player import Player

# User class
class User(Player):
    def __init__(self, name, ID):
        super().__init__(name, ID)
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