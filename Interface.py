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
from kivy.uix.textinput import TextInput
from User import User
from kivy.uix.screenmanager import ScreenManager, Screen

# Home screen
class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

# Login screen
class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.username = self.ids.username
        self.password = self.ids.password

    # gets the user from the database
    def getUser(self):  # FIXME finish
        username = self.username.text
        password = self.password.text

# CreateUser Screen
class CreateUser(Screen):
    def __init__(self, **kwargs):
        super(CreateUser, self).__init__(**kwargs)
        self.username = self.ids.username
        self.password = self.ids.password

    # creates the user and adds them to the database
    def createUser(self):  # FIXME finish
        username = self.username.text
        password = self.password.text

# Dashboard screen
class Dashboard(Screen):
    text = StringProperty(None)
    def __init__(self, User, **kwargs):
        self.User = User
        self.text = self.User.name
        super(Dashboard, self).__init__(**kwargs)

# Group screen
class Group(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)

# AdminGroup screen
class AdminGroup(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(AdminGroup, self).__init__(**kwargs)

# BeerPong screen
class BeerPong(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(BeerPong, self).__init__(**kwargs)

# Snappa screen
class Snappa(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(Snappa, self).__init__(**kwargs)

# BPTournament screen
class BeerPongTournament(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(BeerPongTournament, self).__init__(**kwargs)

# SnappaTournament screen
class SnappaTournament(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(SnappaTournament, self).__init__(**kwargs)

# BPLeague screen
class BeerPongLeague(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(BeerPongLeague, self).__init__(**kwargs)

# SnappaLeague screen
class SnappaLeague(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(SnappaLeague, self).__init__(**kwargs)

# Team screen
class Team(Screen):
    prev = StringProperty('dashboard')
    def __init__(self, **kwargs):
        super(Team, self).__init__(**kwargs)

# WindowManager Class
class WindowManager(ScreenManager):
    pass

# Interface class the main app that runs upon initialization of the program
class Interface(App):
    user = None
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Home(name='home'))
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(CreateUser(name='create_user'))
        self.sm.add_widget(Group(name='group'))
        self.sm.add_widget(AdminGroup(name='admin_group'))
        self.sm.add_widget(BeerPong(name='beer_pong'))
        self.sm.add_widget(Snappa(name='snappa'))
        self.sm.add_widget(BeerPongTournament(name='beer_pong_tournament'))
        self.sm.add_widget(SnappaTournament(name='snappa_tournament'))
        self.sm.add_widget(BeerPongLeague(name='beer_pong_league'))
        self.sm.add_widget(SnappaLeague(name='snappa_league'))
        self.sm.add_widget(Team(name='team'))
        return self.sm

    # creates a user, adds them to database, and creates a dashboard for them
    def createUser(self, username, password):
        print(username," ", password)
        self.user = User(username, "add_ID")
        self.sm.add_widget(Dashboard(self.user, name='dashboard'))

    # grabs a user from the database, and creates a dashboard for them
    def getUser(self, username, password):
        print(username," ", password)
        self.user = User(username, "add_ID")
        self.sm.add_widget(Dashboard(self.user, name='dashboard'))