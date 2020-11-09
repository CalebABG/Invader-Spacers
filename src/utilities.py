import sys

import pygame
import random

from alien import Alien
from particle import Particle


GAME_STATE = 0
GAME_FRAME_RATE = 78
GAME_RUNNING = True
GAME_WINDOW = None
GAME_CLOCK = None
GAME_DELTA = None
GAME_COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "violet": (100, 0, 130),
    "majestic blue": (22, 10, 57),  # Default value = (22, 10, 57)
    "white": (255, 255, 255)
}


def end_session():
    pygame.quit()
    sys.exit()


def draw_message(surface, msg, paint, font_size, x, y):
    font = pygame.font.SysFont("monospace", font_size)
    surface.blit(font.render(msg, True, paint), [x, y])


def draw_particles(width, height, color, background_sprite_group):
    for number in range(0, 3):  # Default value is (0, 3)

        """ Creates a random color for the sprite """
        # randomcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        """ Creates a random speed for the sprite """
        rand_speed = (random.randrange(4, 15))

        """ Creates random sizes for the sprites """
        rand_width = random.randrange(0, 3)  # Default value is (0, 3)
        rand_height = random.randrange(0, 6)  # Default value is (0, 6)

        """ Creates two random location variables for the x and y positions on the screen """
        rand_x = random.randrange(0, width - rand_width)
        rand_y = random.randrange(0, height - rand_height)

        """ Creates a particle object and assigns it a color and a size """
        particle = Particle(color, rand_width, rand_height)

        """ Sets the position for the sprites """
        particle.set_position(rand_x, 2)

        """ Adds sprites to all_sprites group """
        background_sprite_group.add(particle)

        """ Adds gravity to sprites """
        gravity = rand_speed
        if particle.v_speed == 0:
            particle.v_speed += gravity

        """ Loop to kill sprites """
        for sprite in background_sprite_group:
            if sprite.rect.y > height or sprite.rect.y < 0:
                background_sprite_group.remove(sprite)


def draw_aliens(width, height, alien_sprite_group, player_sprite, player_sprite_group):
    for x in range(0, 2):  # Default value is (0, 3)
        random_speed = random.randrange(1, 3)
        rand_x = random.randrange(20, width - 31)
        rand_y = random.randrange(0, height - 22)

        aliens = Alien(width, height, player_sprite, player_sprite_group)
        aliens.set_position(rand_x, rand_y - 800)
        aliens.change_speed(0, random_speed)

        alien_sprite_group.add(aliens)


def draw_resolution_menu(window, ft):
    game_mode_selection = -1

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    mx, my = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]

    window.fill((255, 211, 107))

    draw_message(window, "Resolution Select", (255, 61, 61), 60, 77, 10)
    draw_message(window, "Default Screen", (0, 0, 153), 37, 20, 130)
    draw_message(window, "Large Screen", (255, 0, 0), 37, 20, 300)

    """ 
    Credit: Jeremy Gagnier @ http://jergagnier.wix.com/projects
    Borrowed code for selectable buttons (re-named things, but credit given to creator) 
    """
    # Button for res mode 1
    res_1_text = "750 x 650"
    game_select_one = ft.render(res_1_text, True, (0, 0, 120)), ft.size(res_1_text)

    window.blit(game_select_one[0], (530 - game_select_one[1][0] / 2, 150 - game_select_one[1][1] / 2))

    if 530 - game_select_one[1][0] / 2 < mx < 530 + game_select_one[1][0] / 2 and \
            150 - game_select_one[1][1] / 2 < my < 150 + game_select_one[1][1] / 2:
        pygame.draw.rect(window, (0, 0, 153), [530 - game_select_one[1][0] / 2 - 10,
                                               150 - game_select_one[1][1] / 2,
                                               game_select_one[1][0] + 20,
                                               game_select_one[1][1] - 10], 4)
        if mouse_clicked:
            game_mode_selection = 0

    # Button for res mode 2
    res_2_text = "850 x 750"
    game_select_two = ft.render(res_2_text, True, (0, 0, 255)), ft.size(res_2_text)
    window.blit(game_select_two[0], (530 - game_select_two[1][0] / 2, 320 - game_select_two[1][1] / 2))

    if 530 - game_select_two[1][0] / 2 < mx < 530 + game_select_two[1][0] / 2 and \
            320 - game_select_two[1][1] / 2 < my < 320 + game_select_two[1][1] / 2:
        pygame.draw.rect(window, (255, 0, 0), [530 - game_select_two[1][0] / 2 - 10,
                                               320 - game_select_two[1][1] / 2,
                                               game_select_two[1][0] + 20,
                                               game_select_two[1][1] - 10], 4)
        if mouse_clicked:
            game_mode_selection = 1

    # Button for res mode 3
    res_3_text = "Sand Box Mode"
    game_select_three = ft.render(res_3_text, True, (0, 0, 255)), ft.size(res_3_text)
    window.blit(game_select_three[0], (380 - game_select_three[1][0] / 2, 500 - game_select_three[1][1] / 2))

    if 330 - game_select_three[1][0] / 2 < mx < 330 + game_select_three[1][0] / 2 \
            and 500 - game_select_three[1][1] / 2 < my < 500 + game_select_three[1][1] / 2:
        pygame.draw.rect(window, (0, 0, 210), [380 - game_select_three[1][0] / 2 - 10,
                                               500 - game_select_three[1][1] / 2,
                                               game_select_three[1][0] + 20,
                                               game_select_three[1][1] - 10], 4)
        if mouse_clicked:
            game_mode_selection = 2

    return game_mode_selection
