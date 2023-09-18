TIME_ROTATE = 20
FPS = 60
LEVEL = 2
SCORE = 0
NB_LIGNE = 0
SENS = 0

#info plateau de jeu:
PIXEL_SIZE = 25
PIXEL_SIZE_BACKROUND = 20
NB_LIG = 20
NB_COl = 10
LEVEL_WIDTH = NB_COl * PIXEL_SIZE
LEVEL_HEIGTH = NB_LIG * PIXEL_SIZE

#taille fenetre:
WIDTH = LEVEL_WIDTH * 3
HEIGTH = LEVEL_HEIGTH

#plateau
PLATEAU = []
for i in range(NB_COl):
    lig = []
    for j in range(NB_LIG):
        lig.append(" ")
    PLATEAU.append(lig)


#couleurs:
LIGHT_BLUE = (135, 206, 235)
BLUE = (27, 66, 229)
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLEU_7 = (93, 34, 205)
RED_7 = (93, 0, 54)
BLEU_5 = (95, 109, 155)
BLANC_5 =(95, 109, 155)
VERT_5 = (80, 203, 128)
BLANC_6 = (202, 143, 136)
BLEU_6 = (102, 102, 102)
ORANGE = (230, 161, 27)
VERT_0 = (106, 175, 253)
BLEU_0 = (68, 59, 236)
ORANGE_1 = (137, 215, 2)
VERT_1 = (10, 140, 1)
LIGHT_1 = (106, 147, 100)
BLUE_2 = (157, 27, 205)
LIGHT_BLUE_2 = (219, 94, 229)
ORANGE_3 = (94, 225, 52)
BLEU_3 = (64, 60, 243)
ROSE_4 = (157, 104, 145)
VERT_4 = (61, 200, 119)
VIOLET = (175, 28, 115)

#couleur des pèces pour chaque niveau:
I = {0:LIGHT_BLUE, 1:LIGHT_1, 2:LIGHT_BLUE, 3:LIGHT_BLUE, 4:ROSE_4, 5:BLANC_5, 6:BLANC_6, 7:LIGHT_BLUE, 8:LIGHT_BLUE, 9:BLANC_6}
O = {0:LIGHT_BLUE, 1:LIGHT_1, 2:LIGHT_BLUE, 3:LIGHT_BLUE, 4:ROSE_4, 5:BLANC_5, 6:BLANC_6, 7:LIGHT_BLUE, 8:LIGHT_BLUE, 9:BLANC_6}
T = {0:LIGHT_BLUE, 1:LIGHT_1, 2:LIGHT_BLUE, 3:LIGHT_BLUE, 4:ROSE_4, 5:BLANC_5, 6:BLANC_6, 7:LIGHT_BLUE, 8:LIGHT_BLUE, 9:BLANC_6}
L = {0:VERT_0, 1:ORANGE_1, 2:LIGHT_BLUE_2, 3:ORANGE_3, 4:VERT_4, 5:BLEU_5, 6:BLEU_6, 7:RED_7, 8:RED, 9:ORANGE}
J = {0:BLEU_0, 1:VERT_1, 2:BLUE_2, 3:BLEU_3, 4:VIOLET, 5:VERT_5, 6:RED, 7:BLEU_7, 8:BLUE, 9:RED}
S = {0:BLEU_0, 1:VERT_1, 2:BLUE_2, 3:BLEU_3, 4:VIOLET, 5:VERT_5, 6:RED, 7:BLEU_7, 8:BLUE, 9:RED}
Z = {0:VERT_0, 1:ORANGE_1, 2:LIGHT_BLUE_2, 3:ORANGE_3, 4:VERT_4, 5:BLEU_5, 6:BLEU_6, 7:RED_7, 8:RED, 9:ORANGE}


VITESSE = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 4, 3, 2, 1]
COULEUR = [J, L, I, T, O, S, Z]

#docu:
#https://tetris.wiki/Tetris_(NES,_Nintendo)
#https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318


