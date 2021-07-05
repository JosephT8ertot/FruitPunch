"""
Creator: Joseph A Tate
Last Edit: 6/25/2021
    Teams maintain the players and stats for teams of different games. A general team is a team that works with all
game types.
"""


# imports

# Team class (general team)
class Team:
    def __init__(self, name, ID, members):
        self.name = name
        self.ID = ID
        self.members = members
        self.beerPongStats = self.loadBPStats()
        self.snappaStats = self.loadSnappaStats()

    # loads the beer pong stats
    def loadBPStats(self):
        pass

    # loads the snappa stats
    def loadSnappaStats(self):
        pass

    # saves all stats
    def saveStats(self):
        pass

    # adds member if doesn't already exist, else returns exception
    def addMember(self, member):
        if member not in self.members:
            self.members.append(member)
        else:
            return Exception('Member already exists.')

    # deletes member from the team
    def deleteMember(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            return Exception('No such member exists')

