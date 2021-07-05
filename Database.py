"""
Creator: Joseph A Tate
Last Edit: 7/5/2021
    The purpose of this class is to give other classes an easy way to connect and load/save data to the mySQL server.
"""

# imports
from mysql import connector

# Database class
class Database:
    def __init__(self, hostname, username, password):
        # creates the connection to the mySQL server
        mydb = connector.connect(
            host=hostname,
            user=username,
            password=password,
            database='FruitPunch'
        )

        # creates the handler for the connection
        self.cursor = mydb.cursor()

db = Database('localhost','root','BNM!@#bnm123')