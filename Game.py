"""
Creator: Joseph A Tate
Last Edit: 6/26/2021
    This class contains the games for different types of games. It contains a regular and node version for each game
type.
"""


# imports

# Game class
class Game:
    def __init__(self, name, ID, teams):
        self.name = name
        self.ID = ID
        self.teams = teams

# SnappaGame class
class SnappaGame:
    def __init__(self, name, ID, teams=(None, None)):
        super().__init__(self, name, ID, teams)
        self.stats = {'throws':0,'hits':0,'sinks':0,'scores':0,'catches':0,'drops':0,'wins':0,'losses':0}

class BeerPongGame:
    def __init__(self, name, ID, teams=(None, None)):
        super().__init__(self, name, ID, teams)
        self.stats = {'shots':0,'sinks':0,'wins':0,'losses':0}