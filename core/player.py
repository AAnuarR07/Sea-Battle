from core.abilities import Nuke
from core.abilities import Submarine
from core.board import Board

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.shots = []

        self.nuke = Nuke()
        self.submarine = Submarine()