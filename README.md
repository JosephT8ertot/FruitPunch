# FruitPunch

## Overview
FruitPunch is a software application that allows it's users to track or play all sorts of drinking games on the big screen!
### Players
FruitPunch maintains a database of player statistics online. FruitPunch players are not online but rather exist permanently or temporarily in a group, and can be added into games, leagues, and tournaments to play against each other on ranked or unranked matches!
### Users
FruitPunch Users are players that can personally sign in and view their stats at any time, anywhere! Users can create and maintain games, tournaments, groups etc.
### Groups
FruitPunch users can create temporary or permanent groups of users and players with a permission based structure. These groups can then pit their users and players against each other in all sorts of tournaments and ranked or unranked matches.
### Games
FruitPunch can play and rank player and user statistics on many games such as:
 * Beer Pong
 * Snappa
 * Rage Cage
 * Kings / Other Card Games
 * Flip Cup
### Tournaments / Leagues
FruitPunch gives groups the ability to create leagues and tournaments! Tournaments can be random or set up in a specific order and can pit players against each other until a single winner is determined. Leagues can pit players together in a random or specific order and over time the statistics of the players will determine the winner(s) of the tournament. Statistics of either tournaments or leagues can be displayed at any time.
### Statistics
FruitPunch tracks player statistics for users, groups, and across the world to give users a fully immersed experience with the world of drinking games. Users can pit themselves in skill against players from Italy, China, the US, Brasil, etc.

## Code
### Classes and Files
 * FuitPunch - Runs at start of App
 * Interface - Controls the user interface classes, pages, etc.
 * interface.kv - Kivy file for the user interface and interface pages
 * Player - Controls the layer and their stats
 * User - Controls the user and their stats
 * Group - Controls the stats, tournaments, leagues, and users for a group. Can have one or more admins.
 * Game - Contains the classes for each game
 * Tournament - Controls a tournament and stats for x users
 * League - Controls a league and stats for x users
### FruitPunch
 * Simply runs the start of the Interface. Can run test cases during development.
### Interface
 * Home, Login, Create, Dashboard, Game(all types), Load Group, Create Group, Group, Admin Group, Statistics(all types), Load Tournament, Tournament Create, Tournament, Load League, Create League, League, Screen Manager, FruitPunch are all classes
### interface.kv
 * Has a screen outline for all classes above using FruitPunch as App and ScreenManager as Manager
### Player
 * name, stats
### User
 * name, stats, password, adminGroups, groups
### Group
 * name, stats, users, players, tournaments, leagues
### Game
 * Beer Pong, Snappa, Rage Cage, Kings / Other Card Games, Flip Cup, etc. are classes
 * Each class has own statistics
### Tournament
 * name, stats, users, players
### League
 * name, stats, users, players
