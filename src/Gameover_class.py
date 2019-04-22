import sys
import os

import Resolution_select_class
from BackgroundParticles_class import *
from pygame.locals import *

def endgame():
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

    """ Creates the screen with width, height, and two flags """

    window = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

    """ Creates a fps counter """
    fps_logger = 68  # Default value is 53

    """ Creates a time-keeper variable """
    clock = pygame.time.Clock()

    background_image = pygame.image.load("res/gameover.png").convert_alpha()

    background = BackGroundParticles()
    background_group = pygame.sprite.Group()

    restart = Resolution_select_class.Res_Select()

    game_state = 0

    while running:

        if game_state == 0:

            window.fill((0, 0, 0))
            background.particle_graphics(display_width, display_height, Colors["white"], background_group)

            background_group.draw(window)
            background_group.update()

            window.blit(background_image, (0, 0))

        else:
            restart.start(window)

        """ Event handler """
        for event in pygame.event.get():

            """ Handles escape key event """
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    game_state = 1

        clock.tick(fps_logger)
        pygame.display.set_caption("FPS: %.2d " % (clock.get_fps()))
        pygame.display.update()
