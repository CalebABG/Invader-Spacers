from Game_types import *
from Tools_class import ScreenMessage
from pygame.locals import *

game_type_one = Res_1()
game_type_two = Res_2()
game_type_three = Res_3()


class Res_Select:

    def __init__(self):
        self.window = None

    def start(self, screen):
        self.window = screen

        ft = pygame.font.SysFont("monospace", 66)

        key = pygame.key.get_pressed()
        pygame.event.pump()

        if key[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        mx, my = pygame.mouse.get_pos()
        lc = pygame.mouse.get_pressed()[0]

        self.window.fill((255, 211, 107))

        ScreenMessage(self.window, "Resolution Select", (255, 61, 61), 60, 77, 10)
        ScreenMessage(self.window, "Smaller screen", (0, 0, 153), 37, 20, 130)
        ScreenMessage(self.window, "Default screen", (255, 0, 0), 37, 20, 300)
        # ScreenMessage(self.window, "Larger screen", (0, 0, 153), 37, 20, 480)

        """ 
        Credit: Jeremy Gagnier @ http://jergagnier.wix.com/projects
        Borrowed code for selectable buttons (re-named things, but credit given to creator) 
        """
        # Button for res mode 1
        game_select_one = ft.render('680 x 590', 1, (0, 0, 120)), ft.size('680 x 590')
        self.window.blit(game_select_one[0], (530 - game_select_one[1][0] / 2, 150 - game_select_one[1][1] / 2))

        if 530 - game_select_one[1][0] / 2 < mx < 530 + game_select_one[1][0] / 2 and \
                150 - game_select_one[1][1] / 2 < my < 150 + game_select_one[1][1] / 2:
            pygame.draw.rect(self.window, (0, 0, 153), (
                530 - game_select_one[1][0] / 2 - 10, 150 - game_select_one[1][1] / 2, game_select_one[1][0] + 20,
                game_select_one[1][1] - 10), 4)
            if lc:
                game_type_one.game_on()

        # Button for res mode 2
        game_select_two = ft.render('700 x 650', 1, (255, 0, 0)), ft.size('700 x 650')
        self.window.blit(game_select_two[0], (530 - game_select_two[1][0] / 2, 320 - game_select_two[1][1] / 2))

        if 530 - game_select_two[1][0] / 2 < mx < 530 + game_select_two[1][0] / 2 and 320 - game_select_two[1][
            1] / 2 < my < 320 + game_select_two[1][1] / 2:
            pygame.draw.rect(self.window, (255, 0, 0), (
                530 - game_select_two[1][0] / 2 - 10, 320 - game_select_two[1][1] / 2, game_select_two[1][0] + 20,
                game_select_two[1][1] - 10), 4)
            if lc:
                game_type_two.game_on()

        # Button for res mode 3
        game_select_three = ft.render('Sand Box Mode', 1, (0, 0, 255)), ft.size('Sand Box Mode')
        self.window.blit(game_select_three[0], (380 - game_select_three[1][0] / 2, 500 - game_select_three[1][1] / 2))

        if 330 - game_select_three[1][0] / 2 < mx < 330 + game_select_three[1][0] / 2 \
                and 500 - game_select_three[1][1] / 2 < my < 500 + game_select_three[1][1] / 2:
            pygame.draw.rect(self.window, (0, 0, 210), (
                380 - game_select_three[1][0] / 2 - 10, 500 - game_select_three[1][1] / 2, game_select_three[1][0] + 20,
                game_select_three[1][1] - 10), 4)
            if lc:
                game_type_three.game_on()
