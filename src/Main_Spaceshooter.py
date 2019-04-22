import sys
import os
from BackgroundParticles_class import *
from pygame.locals import *
from Resolution_select_class import *
import pygame

""" Method which loads all pygame modules """
pygame.init()

""" Colors """
Colors = {"red": (255, 0, 0),
          "green": (0, 255, 0),
          "blue": (0, 0, 255),
          "black": (0, 0, 0),
          "violet": (100, 0, 130),
          "majestic blue": (22, 10, 57),  # Default value = (22, 10, 57)
          "white": (255, 255, 255)}

""" creates a variable to hold the width and height of the screen """
os.environ['SDL_VIDEO_CENTERED'] = '1'
display_size = display_width, display_height = 750, 650

""" Running variable """
running = True


def end_session():
    pygame.quit()
    sys.exit()


""" Creates the screen with width, height, and two flags """
pygame.display.set_icon(pygame.image.load('res/icon.png'))
window = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

""" Creates a fps counter """
fps_logger = 68  # Default value is 53

""" Creates a time-keeper variable """
clock = pygame.time.Clock()

dt = clock.tick(fps_logger)

res_menu = Res_Select()

background_image = pygame.image.load("res/start screen.png").convert_alpha()

background = BackGroundParticles()
background_group = pygame.sprite.Group()

ft_1 = pygame.font.SysFont("monospace", 62)

x = display_width / 2
y = 575

width = 6
height = 1

game_state = 0


def welcome():
    global game_state

    mx, my = pygame.mouse.get_pos()
    lc = pygame.mouse.get_pressed()[0]

    window.fill((0, 0, 0))
    background.particle_graphics(display_width, display_height, Colors["white"], background_group)

    background_group.draw(window)
    background_group.update()

    window.blit(background_image, (0, 0))

    """ Borrowed code for selectable buttons (re-named things, but credit given to creator) """
    game_select_one = ft_1.render('Click here to play!', 1, (255, 0, 0)), ft_1.size('Click here to play!')

    window.blit(game_select_one[0], (x - game_select_one[1][0] / 2, y - game_select_one[1][1] / 2))
    if x - game_select_one[1][0] / 2 < mx < x + game_select_one[1][0] / 2 and y - game_select_one[1][1] / 2 < my < y + \
            game_select_one[1][1] / 2:
        pygame.draw.rect(window, (45, 43, 43), (x - game_select_one[1][0] / 2 - 10,  # X
                                                y - game_select_one[1][1] / 2 + 2,  # Y
                                                game_select_one[1][0] + width,  # Width
                                                game_select_one[1][1] + height), 4)  # Height and thickness
        if lc:
            game_state = 1

    return game_state


""" GAME LOOP """
""" *** NOTE TO SELF: DO NOT CREATE VARIABLES IN GAME LOOP, WILL DIMINISH FPS AND CAUSE PROBLEMS *** """
while running:

    """ Event handler """
    for event in pygame.event.get():
        """ Handles escape key event """
        if event.type == pygame.event:
            running = False
            end_session()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.K_ESCAPE:
                end_session()

    if game_state == 0:
        welcome()

    else:
        res_menu.start(window)
        key = pygame.key.get_pressed()
        pygame.event.pump()

    clock.tick(fps_logger)
    pygame.display.set_caption("FPS: %.2d " % (clock.get_fps()))
    pygame.display.update()
