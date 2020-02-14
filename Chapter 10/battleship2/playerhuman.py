import random
from player import Player
from grid import Grid

# Provides Ai Player
class PlayerHuman(Player):

    def __init__ (self):
        Player.__init__(self)