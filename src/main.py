import os
import pygame
import game
import utilities

""" Method which loads all pygame modules """
pygame.init()

""" creates a variable to hold the width and height of the screen """
os.environ['SDL_VIDEO_CENTERED'] = '1'

display_size = 750, 650

""" Creates the screen with width, height, and two flags """
pygame.display.set_icon(pygame.image.load('res/icon.png'))

utilities.GAME_WINDOW = pygame.display.set_mode(display_size, pygame.DOUBLEBUF, 32)

""" Creates a time-keeper variable """
utilities.GAME_CLOCK = pygame.time.Clock()

utilities.GAME_DELTA = utilities.GAME_CLOCK.tick(utilities.GAME_FRAME_RATE)

background_image = pygame.image.load("res/start screen.png").convert_alpha()
gameover_image = pygame.image.load("res/gameover.png").convert_alpha()

background_group = pygame.sprite.Group()

game_font = pygame.font.SysFont("monospace", 52)
current_game = None

window_size = pygame.display.get_window_size()
x = window_size[0] / 2
y = 575

width = 6
height = 1


def welcome():
    mx, my = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]

    display_width, display_height = pygame.display.get_window_size()
    utilities.GAME_WINDOW.fill((0, 0, 0))
    utilities.draw_particles(display_width, display_height, utilities.GAME_COLORS["white"], background_group)

    background_group.draw(utilities.GAME_WINDOW)
    background_group.update()

    utilities.GAME_WINDOW.blit(background_image, (0, 0))

    """ Borrowed code for selectable buttons (re-named things, but credit given to creator) """
    render_message = "Click here to play!"
    game_select_one = game_font.render(render_message, True, (255, 0, 0)), game_font.size(render_message)

    utilities.GAME_WINDOW.blit(game_select_one[0], (x - game_select_one[1][0] / 2, y - game_select_one[1][1] / 2))
    if x - game_select_one[1][0] / 2 < mx < x + game_select_one[1][0] / 2 and \
            y - game_select_one[1][1] / 2 < my < y + game_select_one[1][1] / 2:
        pygame.draw.rect(utilities.GAME_WINDOW, (45, 43, 43), [x - game_select_one[1][0] / 2 - 10,  # X
                                                               y - game_select_one[1][1] / 2 + 2,  # Y
                                                               game_select_one[1][0] + width,  # Width
                                                               game_select_one[1][1] + height],
                         4)  # Height and thickness
        if mouse_clicked:
            utilities.GAME_STATE = 1


def gameover():
    display_width, display_height = pygame.display.get_window_size()
    utilities.GAME_WINDOW.fill((0, 0, 0))
    utilities.draw_particles(display_width, display_height, utilities.GAME_COLORS["white"], background_group)

    background_group.draw(utilities.GAME_WINDOW)
    background_group.update()

    utilities.GAME_WINDOW.blit(gameover_image, (0, 0))

    key = pygame.key.get_pressed()

    if key[pygame.K_r]:
        utilities.GAME_STATE = 0


""" GAME LOOP """
""" NOTE TO SELF: DO NOT CREATE VARIABLES IN GAME LOOP, WILL DIMINISH FPS AND CAUSE PROBLEMS """
while utilities.GAME_RUNNING:
    """ Event handler """
    for event in pygame.event.get():
        """ Handles escape key event """
        if event.type == pygame.QUIT:
            utilities.GAME_RUNNING = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                utilities.GAME_RUNNING = False

    if utilities.GAME_STATE == 0:
        welcome()

    elif utilities.GAME_STATE == 1:
        mode = utilities.draw_resolution_menu(utilities.GAME_WINDOW, game_font)
        if mode != -1:
            if mode == 0:
                current_game = game.Game()
            elif mode == 1:
                current_game = game.Game(850, 750)
            elif mode == 2:
                current_game = game.Game(shield_mode=2)

            utilities.GAME_STATE = 2

    elif utilities.GAME_STATE == 2:
        current_game.run()

    elif utilities.GAME_STATE == 3:
        gameover()

    utilities.GAME_DELTA = utilities.GAME_CLOCK.tick(utilities.GAME_FRAME_RATE)
    pygame.display.update()

utilities.end_session()
