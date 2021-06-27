"""
Creator: Joseph A Tate
Last Edit: 6/26/2021
    Interface class contains many classes that helps provides the users with a fluid experience. It is focused around
being easy on the eye, functionality, and drawing the users attention. It makes use of user statistics to make the user
curious.
"""


# imports
from kivy.app import App
from kivy.properties import StringProperty
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
    prev = StringProperty('dashboard')

# AdminGroup screen
class AdminGroup(Screen):
    prev = StringProperty('dashboard')

# BeerPong screen
class BeerPong(Screen):
    prev = StringProperty('dashboard')

# Snappa screen
class Snappa(Screen):
    prev = StringProperty('dashboard')

# BPTournament screen
class BeerPongTournament(Screen):
    prev = StringProperty('dashboard')

# SnappaTournament screen
class SnappaTournament(Screen):
    prev = StringProperty('dashboard')

# BPLeague screen
class BeerPongLeague(Screen):
    prev = StringProperty('dashboard')

# SnappaLeague screen
class SnappaLeague(Screen):
    prev = StringProperty('dashboard')

# Team screen
class Team(Screen):
    prev = StringProperty('dashboard')

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
