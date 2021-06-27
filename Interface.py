"""
Creator: Joseph A Tate
Last Edit: 6/24/2021
    Interface class contains many classes that helps provides the users with a fluid experience. It is focused around
being easy on the eye, functionality, and drawing the users attention. It makes use of user statistics to make the user
curious.
"""


# imports
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# Home screen
class Home(Screen):
    pass

# Login screen
class Login(Screen):
    pass

# CreateUser Screen
class CreateUser(Screen):
    pass

# Dashboard screen
class Dashboard(Screen):
    pass

# Group screen
class Group(Screen):
    pass

# AdminGroup screen
class AdminGroup(Screen):
    pass

# BeerPong screen
class BeerPong(Screen):
    pass

# Snappa screen
class Snappa(Screen):
    pass

# BPTournament screen
class BeerPongTournament(Screen):
    pass

# SnappaTournament screen
class SnappaTournament(Screen):
    pass

# BPLeague screen
class BeerPongLeague(Screen):
    pass

# SnappaLeague screen
class SnappaLeague(Screen):
    pass

# Team screen
class Team(Screen):
    pass

# WindowManager Class
class WindowManager(ScreenManager):
    pass

# Interface class the main app that runs upon initialization of the program
class Interface(App):
    def build(self):
        pass

# Kivy environment variables
Window.minimum_height = 600
Window.minimum_width = 900