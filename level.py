import pygame
from tetris import Tetris
from settings import *
from pieces import *

class Level:

    def __init__(self, ligne):
        self.display_surface = pygame.display.get_surface()
        self.compteur_descente = 0
        self.compteur = 0
        self.counter = 0
        self.tetris = Tetris(NB_COl, NB_LIG, ligne)
        self.tetris.piece_sortie[self.tetris.type_stock] += 1
        self.level = self.tetris.level
        self.fps = self.vitesse()
        self.fast_down = False


    def run(self):
        self.tetris.level = self.tetris.nb_ligne // 10
        self.level = self.tetris.level

        self.affiche_backround()
        self.affiche_piece_stock()
        self.affiche_pieces_sortie()
        self.affiche_plateau()
        self.affiche_piece()
        self.update()

    def game_over(self):

        font_2 = pygame.font.Font('Tetris.ttf', 150)
        text_fin_1 = font_2.render("GAME", True, RED)
        text_fin_2 = font_2.render("OVER", True, RED)

        pygame.draw.rect(self.display_surface, BLACK, (0, 0, WIDTH, HEIGTH))
        self.display_surface.blit(text_fin_1, (PIXEL_SIZE * 6, PIXEL_SIZE * 3))
        self.display_surface.blit(text_fin_2, (PIXEL_SIZE * 6, PIXEL_SIZE * 10))

    def affiche_backround(self):
        pygame.draw.rect(self.display_surface, BLACK, (PIXEL_SIZE * 21.75, PIXEL_SIZE * 0.5, PIXEL_SIZE * 7, PIXEL_SIZE * 5.5))
        pygame.draw.rect(self.display_surface, BLACK, (PIXEL_SIZE * 21.75, PIXEL_SIZE * 15, PIXEL_SIZE * 7, PIXEL_SIZE * 3))
        pygame.draw.rect(self.display_surface, BLACK, (PIXEL_SIZE * 21.75, PIXEL_SIZE * 7, PIXEL_SIZE * 7, PIXEL_SIZE * 7))
        pygame.draw.rect(self.display_surface, BLACK, (PIXEL_SIZE, PIXEL_SIZE * 4.5, PIXEL_SIZE * 8, PIXEL_SIZE * 14.5))
        pygame.draw.rect(self.display_surface, BLACK, (PIXEL_SIZE, PIXEL_SIZE * 0.5, PIXEL_SIZE * 8, PIXEL_SIZE * 3))


    def affiche_piece_sortie(self,type, x, y):
        for i in range(4):
            for j in range(4):
                if PIECE[type][0][i][j] != " ":
                    pygame.draw.rect(self.display_surface, COULEUR[type][self.level % 10],
                                     [x + 4 * PIXEL_SIZE_BACKROUND + PIXEL_SIZE_BACKROUND * j + 1,
                                      y + PIXEL_SIZE_BACKROUND * i+ 1,
                                      PIXEL_SIZE_BACKROUND-2, PIXEL_SIZE_BACKROUND-2])

    def affiche_pieces_sortie(self):
        self.affiche_piece_sortie(3, -PIXEL_SIZE, PIXEL_SIZE * 5)
        self.affiche_piece_sortie(0, -PIXEL_SIZE, PIXEL_SIZE * 7)
        self.affiche_piece_sortie(6, -PIXEL_SIZE, PIXEL_SIZE * 9)
        self.affiche_piece_sortie(4, -PIXEL_SIZE, PIXEL_SIZE * 11)
        self.affiche_piece_sortie(5, -PIXEL_SIZE, PIXEL_SIZE * 13)
        self.affiche_piece_sortie(1, -PIXEL_SIZE, PIXEL_SIZE * 15)
        self.affiche_piece_sortie(2, -PIXEL_SIZE, PIXEL_SIZE * 16 + PIXEL_SIZE * 0.5)


    def affiche_piece_stock(self):
        for i in range(4):
            for j in range(4):
                if PIECE[self.tetris.type_stock][0][i][j] != " ":
                    pygame.draw.rect(self.display_surface, COULEUR[self.tetris.type_stock][self.level % 10],
                                     [LEVEL_WIDTH * 2 + 3.5 * PIXEL_SIZE + PIXEL_SIZE * j + 1,
                                      PIXEL_SIZE * 10 + PIXEL_SIZE * i+ 1,
                                      PIXEL_SIZE-2, PIXEL_SIZE-2])


    def affiche_piece(self):
        for i in range(4):
            for j in range(4):
                if self.tetris.piece.image(i, j) != " ":
                    pygame.draw.rect(self.display_surface, self.tetris.piece.couleur,
                                     [self.tetris.x + PIXEL_SIZE * (j + self.tetris.piece.x) + 1,
                                      self.tetris.y + PIXEL_SIZE * (i + self.tetris.piece.y) + 1,
                                      PIXEL_SIZE-2, PIXEL_SIZE-2])

    def affiche_plateau(self):
        for i in range(self.tetris.height):
            for j in range(self.tetris.width):
                pygame.draw.rect(self.display_surface, BLACK,
                                 [self.tetris.x + PIXEL_SIZE * j, self.tetris.y + PIXEL_SIZE * i,
                                  PIXEL_SIZE,
                                  PIXEL_SIZE])
                if self.tetris.plateau[i][j] == "i":
                    pygame.draw.rect(self.display_surface, I[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1, PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "o":
                    pygame.draw.rect(self.display_surface, O[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "j":
                    pygame.draw.rect(self.display_surface, J[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "l":
                    pygame.draw.rect(self.display_surface, L[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "s":
                    pygame.draw.rect(self.display_surface, S[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "z":
                    pygame.draw.rect(self.display_surface, Z[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                elif self.tetris.plateau[i][j] == "t":
                    pygame.draw.rect(self.display_surface, T[self.level % 10],
                                     [self.tetris.x + PIXEL_SIZE * j + 1, self.tetris.y + PIXEL_SIZE * i + 1,
                                      PIXEL_SIZE - 2,
                                      PIXEL_SIZE - 2])
                else:
                    pygame.draw.rect(self.display_surface, BLACK,
                                     [self.tetris.x + PIXEL_SIZE * j, self.tetris.y + PIXEL_SIZE * i,
                                      PIXEL_SIZE,
                                      PIXEL_SIZE])


    def vitesse(self):
        if self.level <= 10:
            self.fps = VITESSE[self.level]
        elif self.level >= 10 and self.level <= 12:
            self.fps = VITESSE[10]
        elif self.level >= 13 and self.level <= 15:
            self.fps = VITESSE[11]
        elif self.level >= 16 and self.level <= 18:
            self.fps = VITESSE[12]
        elif self.level >= 19 and self.level <= 28:
            self.fps = VITESSE[13]
        elif self.level >= 29:
            self.fps = VITESSE[14]


    def vitesse_1(self):
        if self.fast_down:
           if self.counter == VITESSE[14]:
               if self.tetris.etat == "start":
                   self.tetris.go_down()
        elif self.compteur_descente == self.fps:
            if self.tetris.etat == "start":
                self.tetris.go_down()


    def update(self):
        if self.compteur_descente == self.fps:
            self.compteur_descente = 0
        else:
            self.compteur_descente += 1

        if self.counter == 1:
            self.counter = 0
        else:
            self.counter += 1
        self.vitesse()
        self.vitesse_1()


