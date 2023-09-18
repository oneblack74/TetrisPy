from pieces import *
from settings import *


class Piece:

    def __init__(self, x = 0, y = 0, num = 0, lvl = 0):
        self.x = x
        self.y = y
        self.sens = 0
        self.type = num
        self.lvl = lvl
        self.couleur = COULEUR[self.type][self.lvl % 10]
        self.leter = LETER[self.type]



    def image(self, i, j):
        return PIECE[self.type][self.sens][i][j]


