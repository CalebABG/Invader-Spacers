from aliens import *
from random import *


class AliensGraphics:
    """ Particle background """

    @staticmethod
    def alien_graphics(width, height, alien_sprite_group, player_sprite, player_sprite_group):
        for x in range(0, 2):  # Default value is (0, 3)
            random_speed = randrange(1, 3)
            rand_x = randrange(20, width - 31)
            rand_y = randrange(0, height - 22)

            aliens = Aliens(width, height, player_sprite, player_sprite_group)
            aliens.set_position(rand_x, rand_y - 800)
            aliens.change_speed(0, random_speed)

            alien_sprite_group.add(aliens)

            # """ Loop to kill sprites """
            # for alien in alien_sprite_group:
            #     if alien.rect.y > height:
            #         alien_sprite_group.remove(alien)
