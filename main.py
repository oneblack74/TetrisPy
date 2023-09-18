import pygame, sys
from settings import *
from level import Level



class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption("Tetris")
        self.surface = pygame.display.get_surface()
        self.affichage = "menu 1"
        self.etat_menu_1 = [False, False]
        self.etat_menu_2 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.etat_menu_3 = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.etat_menu_4 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.level = Level(0)

    def piece_sortie(self, nb, x, y):
        font = pygame.font.Font('Tetris.ttf', PIXEL_SIZE)
        text_piece_sortie_2 = font.render(str(nb), True, RED)

        self.level.display_surface.blit(text_piece_sortie_2, (x, y))

    def pieces_sortie(self):
        self.piece_sortie(self.level.tetris.piece_sortie[3], PIXEL_SIZE * 6.5, PIXEL_SIZE * 5)
        self.piece_sortie(self.level.tetris.piece_sortie[0], PIXEL_SIZE * 6.5, PIXEL_SIZE * 7)
        self.piece_sortie(self.level.tetris.piece_sortie[6], PIXEL_SIZE * 6.5, PIXEL_SIZE * 9)
        self.piece_sortie(self.level.tetris.piece_sortie[4], PIXEL_SIZE * 6.5, PIXEL_SIZE * 11)
        self.piece_sortie(self.level.tetris.piece_sortie[5], PIXEL_SIZE * 6.5, PIXEL_SIZE * 13)
        self.piece_sortie(self.level.tetris.piece_sortie[1], PIXEL_SIZE * 6.5, PIXEL_SIZE * 15)
        self.piece_sortie(self.level.tetris.piece_sortie[2], PIXEL_SIZE * 6.5, PIXEL_SIZE * 17)

    def menu_1(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 9 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 7 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 10:
                        self.etat_menu_1[0] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 9 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 12 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 15:
                        self.etat_menu_1[1] = True
                    else:
                        self.etat_menu_1[0] = False
                        self.etat_menu_1[1] = False

                if pygame.mouse.get_pressed(3)[0]:
                    if self.etat_menu_1[1]:
                        pygame.quit()
                        sys.exit()
                    if self.etat_menu_1[0]:
                        self.affichage = "menu 2"
                        run = False


            self.screen.fill(BLACK)

            font = pygame.font.Font('Tetris.ttf', PIXEL_SIZE * 5)
            text_tetris = font.render("TETRIS", True, WHITE)
            self.level.display_surface.blit(text_tetris, (PIXEL_SIZE * 4.5, PIXEL_SIZE))

            if self.etat_menu_1[0]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 9, PIXEL_SIZE * 7, PIXEL_SIZE * 12, PIXEL_SIZE * 3))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 9.25, PIXEL_SIZE * 7.25, PIXEL_SIZE * 11.5, PIXEL_SIZE * 2.5))
            elif self.etat_menu_1[1]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 9, PIXEL_SIZE * 12, PIXEL_SIZE * 12, PIXEL_SIZE * 3))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 9.25, PIXEL_SIZE * 12.25, PIXEL_SIZE * 11.5, PIXEL_SIZE * 2.5))


            font_2 = pygame.font.Font('Tetris.ttf', PIXEL_SIZE * 2)

            text_quitter = font_2.render("QUITTER", True, WHITE)
            self.level.display_surface.blit(text_quitter, (PIXEL_SIZE * 10, PIXEL_SIZE * 12.5))

            text_jouer = font_2.render("JOUER", True, WHITE)
            self.level.display_surface.blit(text_jouer, (PIXEL_SIZE * 11, PIXEL_SIZE * 7.5))


            pygame.display.update()
            self.clock.tick(FPS)


    def menu_2(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_2[0] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_2[1] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_2[2] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_2[3] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_2[4] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_2[5] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_2[6] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_2[7] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_2[8] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_2[9] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 17.75 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 25 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 1 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 3.75:
                        self.etat_menu_2[10] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 9.25 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 20.75 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 14.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 17.75:
                        self.etat_menu_2[11] = True
                    else:
                        self.etat_menu_2[0] = False
                        self.etat_menu_2[1] = False
                        self.etat_menu_2[2] = False
                        self.etat_menu_2[3] = False
                        self.etat_menu_2[4] = False
                        self.etat_menu_2[5] = False
                        self.etat_menu_2[6] = False
                        self.etat_menu_2[7] = False
                        self.etat_menu_2[8] = False
                        self.etat_menu_2[9] = False
                        self.etat_menu_2[10] = False
                        self.etat_menu_2[11] = False

                if pygame.mouse.get_pressed(3)[0]:
                    if self.etat_menu_2[11]:
                        pygame.quit()
                        sys.exit()
                    if self.etat_menu_2[10]:
                        self.affichage = "menu 3"
                        run = False
                    if self.etat_menu_2[0]:
                        self.affichage = "game"
                        self.level = Level(0)
                        run = False
                    if self.etat_menu_2[1]:
                        self.affichage = "game"
                        self.level = Level(10)
                        run = False
                    if self.etat_menu_2[2]:
                        self.affichage = "game"
                        self.level = Level(20)
                        run = False
                    if self.etat_menu_2[3]:
                        self.affichage = "game"
                        self.level = Level(30)
                        run = False
                    if self.etat_menu_2[4]:
                        self.affichage = "game"
                        self.level = Level(40)
                        run = False
                    if self.etat_menu_2[5]:
                        self.affichage = "game"
                        self.level = Level(50)
                        run = False
                    if self.etat_menu_2[6]:
                        self.affichage = "game"
                        self.level = Level(60)
                        run = False
                    if self.etat_menu_2[7]:
                        self.affichage = "game"
                        self.level = Level(70)
                        run = False
                    if self.etat_menu_2[8]:
                        self.affichage = "game"
                        self.level = Level(80)
                        run = False
                    if self.etat_menu_2[9]:
                        self.affichage = "game"
                        self.level = Level(90)
                        run = False



            self.screen.fill(BLACK)

            # carré 0 à 4
            if self.etat_menu_2[0]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 3, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 3.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[1]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 8, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 8.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[2]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 13, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 13.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[3]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 18, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 18.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[4]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 23, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 23.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))

            # carré 5 à 9
            if self.etat_menu_2[5]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 3, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 3.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[6]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 8, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 8.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[7]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 13, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 13.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[8]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 18, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 18.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_2[9]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 23, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 23.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            #bouton next
            if self.etat_menu_2[10]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 17.75, PIXEL_SIZE * 1, PIXEL_SIZE * 7.25, PIXEL_SIZE * 2.75))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 18, PIXEL_SIZE * 1.25, PIXEL_SIZE * 6.75, PIXEL_SIZE * 2.25))

            #bouton quitter
            if self.etat_menu_2[11]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 9, PIXEL_SIZE * 14.5, PIXEL_SIZE * 12, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 9.25, PIXEL_SIZE * 14.75, PIXEL_SIZE * 11.5, PIXEL_SIZE * 3))

            font_2 = pygame.font.Font('Tetris.ttf', PIXEL_SIZE * 2)

            # quitter
            text_quitter = font_2.render("QUITTER", True, WHITE)
            self.level.display_surface.blit(text_quitter, (PIXEL_SIZE * 10, PIXEL_SIZE * 15.5))

            #niveau
            text_next = font_2.render("NEXT", True, WHITE)
            self.level.display_surface.blit(text_next, (PIXEL_SIZE * 18.5, PIXEL_SIZE * 1.5))

            #ligne de 0 à 4
            text_0 = font_2.render("0", True, WHITE)
            self.level.display_surface.blit(text_0, (PIXEL_SIZE * 4, PIXEL_SIZE * 5.5))
            text_1 = font_2.render("1", True, WHITE)
            self.level.display_surface.blit(text_1, (PIXEL_SIZE * 9, PIXEL_SIZE * 5.5))
            text_2 = font_2.render("2", True, WHITE)
            self.level.display_surface.blit(text_2, (PIXEL_SIZE * 14, PIXEL_SIZE * 5.5))
            text_3 = font_2.render("3", True, WHITE)
            self.level.display_surface.blit(text_3, (PIXEL_SIZE * 19, PIXEL_SIZE * 5.5))
            text_4 = font_2.render("4", True, WHITE)
            self.level.display_surface.blit(text_4, (PIXEL_SIZE * 24, PIXEL_SIZE * 5.5))

            #ligne de 5 à 9
            text_5 = font_2.render("5", True, WHITE)
            self.level.display_surface.blit(text_5, (PIXEL_SIZE * 4, PIXEL_SIZE * 10.5))
            text_6 = font_2.render("6", True, WHITE)
            self.level.display_surface.blit(text_6, (PIXEL_SIZE * 9, PIXEL_SIZE * 10.5))
            text_7 = font_2.render("7", True, WHITE)
            self.level.display_surface.blit(text_7, (PIXEL_SIZE * 14, PIXEL_SIZE * 10.5))
            text_8 = font_2.render("8", True, WHITE)
            self.level.display_surface.blit(text_8, (PIXEL_SIZE * 19, PIXEL_SIZE * 10.5))
            text_9 = font_2.render("9", True, WHITE)
            self.level.display_surface.blit(text_9, (PIXEL_SIZE * 24, PIXEL_SIZE * 10.5))




            pygame.display.update()
            self.clock.tick(FPS)

    def menu_3(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_3[0] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_3[1] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_3[2] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_3[3] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_3[4] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_3[5] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_3[6] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_3[7] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_3[8] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_3[9] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 17.75 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 25 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 1 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 3.75:
                        self.etat_menu_3[10] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 9.25 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 20.75 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 14.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 17.75:
                        self.etat_menu_3[11] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 12 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 1 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 3.75:
                        self.etat_menu_3[12] = True


                    else:
                        self.etat_menu_3[0] = False
                        self.etat_menu_3[1] = False
                        self.etat_menu_3[2] = False
                        self.etat_menu_3[3] = False
                        self.etat_menu_3[4] = False
                        self.etat_menu_3[5] = False
                        self.etat_menu_3[6] = False
                        self.etat_menu_3[7] = False
                        self.etat_menu_3[8] = False
                        self.etat_menu_3[9] = False
                        self.etat_menu_3[10] = False
                        self.etat_menu_3[11] = False
                        self.etat_menu_3[12] = False

                if pygame.mouse.get_pressed(3)[0]:
                    if self.etat_menu_3[11]:
                        pygame.quit()
                        sys.exit()
                    if self.etat_menu_3[10]:
                        self.affichage = "menu 4"
                        run = False
                    if self.etat_menu_3[12]:
                        self.affichage = "menu 2"
                        run = False
                    if self.etat_menu_3[0]:
                        self.affichage = "game"
                        self.level = Level(100)
                        run = False
                    if self.etat_menu_3[1]:
                        self.affichage = "game"
                        self.level = Level(110)
                        run = False
                    if self.etat_menu_3[2]:
                        self.affichage = "game"
                        self.level = Level(120)
                        run = False
                    if self.etat_menu_3[3]:
                        self.affichage = "game"
                        self.level = Level(130)
                        run = False
                    if self.etat_menu_3[4]:
                        self.affichage = "game"
                        self.level = Level(140)
                        run = False
                    if self.etat_menu_3[5]:
                        self.affichage = "game"
                        self.level = Level(150)
                        run = False
                    if self.etat_menu_3[6]:
                        self.affichage = "game"
                        self.level = Level(160)
                        run = False
                    if self.etat_menu_3[7]:
                        self.affichage = "game"
                        self.level = Level(170)
                        run = False
                    if self.etat_menu_3[8]:
                        self.affichage = "game"
                        self.level = Level(180)
                        run = False
                    if self.etat_menu_3[9]:
                        self.affichage = "game"
                        self.level = Level(190)
                        run = False



            self.screen.fill(BLACK)

            # carré 0 à 4
            if self.etat_menu_3[0]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 3, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 3.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[1]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 8, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 8.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[2]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 13, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 13.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[3]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 18, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 18.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[4]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 23, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 23.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))

            # carré 5 à 9
            if self.etat_menu_3[5]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 3, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 3.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[6]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 8, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 8.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[7]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 13, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 13.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[8]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 18, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 18.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_3[9]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 23, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 23.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            #bouton next
            if self.etat_menu_3[10]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 17.75, PIXEL_SIZE * 1, PIXEL_SIZE * 7.25, PIXEL_SIZE * 2.75))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 18, PIXEL_SIZE * 1.25, PIXEL_SIZE * 6.75, PIXEL_SIZE * 2.25))

            #bouton quitter
            if self.etat_menu_3[11]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 9, PIXEL_SIZE * 14.5, PIXEL_SIZE * 12, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 9.25, PIXEL_SIZE * 14.75, PIXEL_SIZE * 11.5, PIXEL_SIZE * 3))

            font_2 = pygame.font.Font('Tetris.ttf', PIXEL_SIZE * 2)

            # bouton prev
            if self.etat_menu_3[12]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 4.75, PIXEL_SIZE * 1, PIXEL_SIZE * 7.25, PIXEL_SIZE * 2.75))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 5, PIXEL_SIZE * 1.25, PIXEL_SIZE * 6.75, PIXEL_SIZE * 2.25))

            # prev
            text_next = font_2.render("PREV", True, WHITE)
            self.level.display_surface.blit(text_next, (PIXEL_SIZE * 5.5, PIXEL_SIZE * 1.5))

            # quitter
            text_quitter = font_2.render("QUITTER", True, WHITE)
            self.level.display_surface.blit(text_quitter, (PIXEL_SIZE * 10, PIXEL_SIZE * 15.5))

            #niveau
            text_next = font_2.render("NEXT", True, WHITE)
            self.level.display_surface.blit(text_next, (PIXEL_SIZE * 18.5, PIXEL_SIZE * 1.5))

            #ligne de 0 à 4
            text_0 = font_2.render("10", True, WHITE)
            self.level.display_surface.blit(text_0, (PIXEL_SIZE * 4, PIXEL_SIZE * 5.5))
            text_1 = font_2.render("11", True, WHITE)
            self.level.display_surface.blit(text_1, (PIXEL_SIZE * 9, PIXEL_SIZE * 5.5))
            text_2 = font_2.render("12", True, WHITE)
            self.level.display_surface.blit(text_2, (PIXEL_SIZE * 14, PIXEL_SIZE * 5.5))
            text_3 = font_2.render("13", True, WHITE)
            self.level.display_surface.blit(text_3, (PIXEL_SIZE * 19, PIXEL_SIZE * 5.5))
            text_4 = font_2.render("14", True, WHITE)
            self.level.display_surface.blit(text_4, (PIXEL_SIZE * 24, PIXEL_SIZE * 5.5))

            #ligne de 5 à 9
            text_5 = font_2.render("15", True, WHITE)
            self.level.display_surface.blit(text_5, (PIXEL_SIZE * 4, PIXEL_SIZE * 10.5))
            text_6 = font_2.render("16", True, WHITE)
            self.level.display_surface.blit(text_6, (PIXEL_SIZE * 9, PIXEL_SIZE * 10.5))
            text_7 = font_2.render("17", True, WHITE)
            self.level.display_surface.blit(text_7, (PIXEL_SIZE * 14, PIXEL_SIZE * 10.5))
            text_8 = font_2.render("18", True, WHITE)
            self.level.display_surface.blit(text_8, (PIXEL_SIZE * 19, PIXEL_SIZE * 10.5))
            text_9 = font_2.render("19", True, WHITE)
            self.level.display_surface.blit(text_9, (PIXEL_SIZE * 24, PIXEL_SIZE * 10.5))




            pygame.display.update()
            self.clock.tick(FPS)

    def menu_4(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_4[0] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_4[1] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_4[2] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_4[3] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 8.25:
                        self.etat_menu_4[4] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 3 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 6.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_4[5] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 8 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 11.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_4[6] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 13 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 16.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_4[7] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 18 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 21.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_4[8] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 23 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 26.5 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 9.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 13.25:
                        self.etat_menu_4[9] = True

                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 4.75 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 12 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 1 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 3.75:
                        self.etat_menu_4[10] = True
                    elif pygame.mouse.get_pos()[0] >= PIXEL_SIZE * 9.25 and pygame.mouse.get_pos()[0] <= PIXEL_SIZE * 20.75 \
                        and pygame.mouse.get_pos()[1] >= PIXEL_SIZE * 14.75 and pygame.mouse.get_pos()[1] <= PIXEL_SIZE * 17.75:
                        self.etat_menu_4[11] = True
                    else:
                        self.etat_menu_4[0] = False
                        self.etat_menu_4[1] = False
                        self.etat_menu_4[2] = False
                        self.etat_menu_4[3] = False
                        self.etat_menu_4[4] = False
                        self.etat_menu_4[5] = False
                        self.etat_menu_4[6] = False
                        self.etat_menu_4[7] = False
                        self.etat_menu_4[8] = False
                        self.etat_menu_4[9] = False
                        self.etat_menu_4[10] = False
                        self.etat_menu_4[11] = False

                if pygame.mouse.get_pressed(3)[0]:
                    if self.etat_menu_4[11]:
                        pygame.quit()
                        sys.exit()
                    if self.etat_menu_4[10]:
                        self.affichage = "menu 3"
                        run = False
                    if self.etat_menu_4[0]:
                        self.affichage = "game"
                        self.level = Level(200)
                        run = False
                    if self.etat_menu_4[1]:
                        self.affichage = "game"
                        self.level = Level(210)
                        run = False
                    if self.etat_menu_4[2]:
                        self.affichage = "game"
                        self.level = Level(220)
                        run = False
                    if self.etat_menu_4[3]:
                        self.affichage = "game"
                        self.level = Level(230)
                        run = False
                    if self.etat_menu_4[4]:
                        self.affichage = "game"
                        self.level = Level(240)
                        run = False
                    if self.etat_menu_4[5]:
                        self.affichage = "game"
                        self.level = Level(250)
                        run = False
                    if self.etat_menu_4[6]:
                        self.affichage = "game"
                        self.level = Level(260)
                        run = False
                    if self.etat_menu_4[7]:
                        self.affichage = "game"
                        self.level = Level(270)
                        run = False
                    if self.etat_menu_4[8]:
                        self.affichage = "game"
                        self.level = Level(280)
                        run = False
                    if self.etat_menu_4[9]:
                        self.affichage = "game"
                        self.level = Level(290)
                        run = False



            self.screen.fill(BLACK)

            # carré 0 à 4
            if self.etat_menu_4[0]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 3, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 3.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[1]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 8, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 8.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[2]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 13, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 13.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[3]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 18, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 18.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[4]:
                pygame.draw.rect(self.surface, WHITE, (PIXEL_SIZE * 23, PIXEL_SIZE * 4.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK, (PIXEL_SIZE * 23.25, PIXEL_SIZE * 5, PIXEL_SIZE * 3, PIXEL_SIZE * 3))

            # carré 5 à 9
            if self.etat_menu_4[5]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 3, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 3.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[6]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 8, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 8.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[7]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 13, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 13.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[8]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 18, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 18.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            if self.etat_menu_4[9]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 23, PIXEL_SIZE * 9.75, PIXEL_SIZE * 3.5, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 23.25, PIXEL_SIZE * 10, PIXEL_SIZE * 3, PIXEL_SIZE * 3))
            #bouton prev
            if self.etat_menu_4[10]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 4.75, PIXEL_SIZE * 1, PIXEL_SIZE * 7.25, PIXEL_SIZE * 2.75))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 5, PIXEL_SIZE * 1.25, PIXEL_SIZE * 6.75, PIXEL_SIZE * 2.25))

            #bouton quitter
            if self.etat_menu_4[11]:
                pygame.draw.rect(self.surface, WHITE,
                                 (PIXEL_SIZE * 9, PIXEL_SIZE * 14.5, PIXEL_SIZE * 12, PIXEL_SIZE * 3.5))
                pygame.draw.rect(self.surface, BLACK,
                                 (PIXEL_SIZE * 9.25, PIXEL_SIZE * 14.75, PIXEL_SIZE * 11.5, PIXEL_SIZE * 3))

            font_2 = pygame.font.Font('Tetris.ttf', PIXEL_SIZE * 2)

            # quitter
            text_quitter = font_2.render("QUITTER", True, WHITE)
            self.level.display_surface.blit(text_quitter, (PIXEL_SIZE * 10, PIXEL_SIZE * 15.5))

            #niveau
            text_next = font_2.render("PREV", True, WHITE)
            self.level.display_surface.blit(text_next, (PIXEL_SIZE * 5.5, PIXEL_SIZE * 1.5))

            #ligne de 0 à 4
            text_0 = font_2.render("20", True, WHITE)
            self.level.display_surface.blit(text_0, (PIXEL_SIZE * 4, PIXEL_SIZE * 5.5))
            text_1 = font_2.render("21", True, WHITE)
            self.level.display_surface.blit(text_1, (PIXEL_SIZE * 9, PIXEL_SIZE * 5.5))
            text_2 = font_2.render("22", True, WHITE)
            self.level.display_surface.blit(text_2, (PIXEL_SIZE * 14, PIXEL_SIZE * 5.5))
            text_3 = font_2.render("23", True, WHITE)
            self.level.display_surface.blit(text_3, (PIXEL_SIZE * 19, PIXEL_SIZE * 5.5))
            text_4 = font_2.render("24", True, WHITE)
            self.level.display_surface.blit(text_4, (PIXEL_SIZE * 24, PIXEL_SIZE * 5.5))

            #ligne de 5 à 9
            text_5 = font_2.render("25", True, WHITE)
            self.level.display_surface.blit(text_5, (PIXEL_SIZE * 4, PIXEL_SIZE * 10.5))
            text_6 = font_2.render("26", True, WHITE)
            self.level.display_surface.blit(text_6, (PIXEL_SIZE * 9, PIXEL_SIZE * 10.5))
            text_7 = font_2.render("27", True, WHITE)
            self.level.display_surface.blit(text_7, (PIXEL_SIZE * 14, PIXEL_SIZE * 10.5))
            text_8 = font_2.render("28", True, WHITE)
            self.level.display_surface.blit(text_8, (PIXEL_SIZE * 19, PIXEL_SIZE * 10.5))
            text_9 = font_2.render("29", True, WHITE)
            self.level.display_surface.blit(text_9, (PIXEL_SIZE * 24, PIXEL_SIZE * 10.5))




            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.level.tetris.rotate_r()
                    if event.key == pygame.K_q:
                        self.level.tetris.rotate_l()
                    if event.key == pygame.K_LEFT:
                        self.level.tetris.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        self.level.tetris.go_side(1)

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.level.fast_down = True
            else:
                self.level.fast_down = False

            self.screen.fill(GREY)

            self.level.run()

            # affichage du backround
            font = pygame.font.Font('Tetris.ttf', 30)

            text_score_1 = font.render("TOP", True, WHITE)
            text_score_2 = font.render(str(self.level.tetris.score), True, WHITE)
            text_score_3 = font.render("SCORE", True, WHITE)
            text_score_4 = font.render(str(self.level.tetris.score), True, WHITE)
            text_level_1 = font.render("LEVEL", True, WHITE)
            text_level_2 = font.render(str(self.level.level), True, WHITE)
            text_next = font.render("NEXT", True, WHITE)
            text_ligne_1 = font.render("LINES", True, WHITE)
            text_ligne_2 = font.render(str(self.level.tetris.nb_ligne), True, WHITE)


            text_score_rect_1 = text_score_2.get_rect(center=(LEVEL_WIDTH * 2 + 5 * PIXEL_SIZE + PIXEL_SIZE * 0.5, PIXEL_SIZE * 2.75))
            text_score_rect_2 = text_score_2.get_rect(center=(LEVEL_WIDTH * 2 + 5 * PIXEL_SIZE + PIXEL_SIZE * 0.5, PIXEL_SIZE * 4 + PIXEL_SIZE * 1.15))


            self.level.display_surface.blit(text_score_1, (LEVEL_WIDTH * 2 + 4 * PIXEL_SIZE, PIXEL_SIZE))
            self.level.display_surface.blit(text_score_2, text_score_rect_1)
            self.level.display_surface.blit(text_score_3, (LEVEL_WIDTH * 2 + PIXEL_SIZE * 3.2, PIXEL_SIZE * 3.5))
            self.level.display_surface.blit(text_score_4, text_score_rect_2)
            self.level.display_surface.blit(text_level_1, (LEVEL_WIDTH * 2 + 3.3 * PIXEL_SIZE, PIXEL_SIZE * 15.5))
            self.level.display_surface.blit(text_level_2, (LEVEL_WIDTH * 2 + 4.8 * PIXEL_SIZE, PIXEL_SIZE * 16.5))
            self.level.display_surface.blit(text_next, (LEVEL_WIDTH * 2 + 3.5 * PIXEL_SIZE, PIXEL_SIZE * 8))
            self.level.display_surface.blit(text_ligne_1, (PIXEL_SIZE * 1.5, PIXEL_SIZE * 1.5))
            self.level.display_surface.blit(text_ligne_2, (PIXEL_SIZE * 6.5, PIXEL_SIZE * 1.5))

            self.pieces_sortie()

            if self.level.tetris.etat == "gameover":
                self.level.game_over()


            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    run = True
    while run:
        if game.affichage == "menu 1":
            game.menu_1()
        if game.affichage == "menu 2":
            game.menu_2()
        if game.affichage == "menu 3":
            game.menu_3()
        if game.affichage == "menu 4":
            game.menu_4()
        if game.affichage == "game":
            game.run()



