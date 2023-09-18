import settings
import random
from piece import *

class Tetris:

    def __init__(self, width, height, nb_ligne = 50):
        self.etat = "start"
        self.width = width
        self.height = height
        self.x = settings.LEVEL_WIDTH
        self.y = 0
        self.type_stock = random.randint(0, len(PIECE) - 1)
        self.type = self.type_stock
        self.score = settings.SCORE
        self.type_start = random.randint(0, len(PIECE) - 1)
        self.piece_sortie = [0, 0, 0, 0, 0, 0, 0]
        self.piece_sortie[self.type_start] += 1
        self.piece_sortie[self.type] -= 1
        self.nb_ligne = nb_ligne
        self.level = (self.nb_ligne // 10) % 10
        self.piece = Piece(3, 0, self.type_start, self.level)
        self.plateau = []
        for i in range(height):
            line = []
            for j in range(width):
                line.append(" ")
            self.plateau.append(line)

    def new_piece(self):
        self.piece = Piece(3,0, self.type, self.level)
        self.piece_sortie[self.type_stock] += 1
        self.type_stock = random.randint(0, len(PIECE) - 1)
        self.type = self.type_stock





    def touche(self):
        toucher = False
        for i in range(4):
            for j in range(4):
                if self.piece.image(i, j) != " ":
                    if i + self.piece.y > self.height - 1 or j + self.piece.x > self.width - 1 or j + self.piece.x < 0 or self.plateau[i + self.piece.y][j + self.piece.x] != " ":
                        toucher = True
        return toucher

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if self.piece.image(i, j) != " ":
                    self.plateau[i + self.piece.y][j + self.piece.x] = self.piece.leter
        self.break_line()
        self.new_piece()
        if self.touche():
            self.etat = "gameover"

    def break_line(self):
        ligne = 0
        for i in range(1, self.height):
            vide = 0
            for j in range(self.width):
                if self.plateau[i][j] == " ":
                    vide += 1
            if vide == 0:
                ligne += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.plateau[i1][j] = self.plateau[i1 - 1][j]
        self.nb_ligne += ligne
        if ligne == 1:
            self.score += (40 * (self.level + 1))
        elif ligne == 2:
            self.score += (100 * (self.level + 1))
        elif ligne == 3:
            self.score += (300 * (self.level + 1))
        elif ligne == 4:
            self.score += (1200 * (self.level + 1))


    def go_down(self):
        self.piece.y += 1
        if self.touche():
            self.piece.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.piece.x
        self.piece.x += dx
        if self.touche():
            self.piece.x = old_x

    def rotate_r(self):
        self.piece.sens = (self.piece.sens - 1) % len(PIECE[self.piece.type][self.piece.sens])
        if self.touche():
            self.piece.sens = (self.piece.sens + 1) % len(PIECE[self.piece.type][self.piece.sens])

    def rotate_l(self):
        self.piece.sens = (self.piece.sens + 1) % len(PIECE[self.piece.type][self.piece.sens])
        if self.touche():
            self.piece.sens = (self.piece.sens - 1) % len(PIECE[self.piece.type][self.piece.sens])
