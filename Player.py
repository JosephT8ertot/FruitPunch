"""
Creator: Joseph A Tate
Last Edit: 6/24/2021
    The player class keeps track of a player name, ID, and stats for different games. Each player has a unique ID
and their stats can be saved for use purposes. But a player in and of itself has less privilege than a User.
"""

# Player class
class Player:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.beerPong = self.loadBPStats()
        self.snappa = self.loadSnappaStats()

    # returns dictionary of stats for player for Beer Pong, returns base dict if player not in database
    def loadBPStats(self):
        return {'shots':0,'sinks':0,'wins':0,'losses':0}

    # returns dictionary of stats for player for Snappa
    def loadSnappaStats(self):
        return {'throws':0,'hits':0,'sinks':0,'scores':0,'catches':0,'drops':0,'wins':0,'losses':0}

    # saves dictionary of stats into player slot in database, creating new slot if player doesn't exist
    def saveStats(self):
        pass  # FIXME add stat save