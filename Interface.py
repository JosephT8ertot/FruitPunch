"""
Creator: Joseph A Tate
Last Edit: 6/24/2021
    Interface class contains many classes that helps provides the users with a fluid experience. It is focused around
being easy on the eye, functionality, and drawing the users attention. It makes use of user statistics to make the user
curious.
"""


# imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Home screen
class Home(Screen):
    pass

# Screen Manager
class WindowManager(ScreenManager):
    pass

# Interface class the main app that runs upon initialization of the program
class Interface(App):
    def build(self):
        pass