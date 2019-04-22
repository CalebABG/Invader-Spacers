import pygame
import random
from Particles_class import *


class BackGroundParticles:
    """ Particle background """

    @staticmethod
    def particle_graphics(width, height, color, background_sprite_group):

        for number in range(0, 3):  # Default value is (0, 3)

            """ Creates a random color for the sprite """
            # randomcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

            """ Creates a random speed for the sprite """
            randspeed = (random.randrange(4, 15))

            """ Creates random sizes for the sprites """
            randsizex = random.randrange(0, 3)  # Default value is (0, 3)
            randsizey = random.randrange(0, 6)  # Default value is (0, 6)

            """ Creates two random location variables for the x and y positions on the screen """
            randlocx = random.randrange(0, width - randsizex)
            randlocy = random.randrange(0, height - randsizey)

            """ Creates a particle object and assigns it a color and a size """
            particle = Particles(color, randsizex, randsizey)

            """ Sets the position for the sprites """
            particle.set_position(randlocx, 2)

            """ Adds sprites to all_sprites group """
            background_sprite_group.add(particle)

            """ Adds gravity to sprites """
            gravity = randspeed
            if particle.vspeed == 0:
                particle.vspeed += gravity

            """ Loop to kill sprites """
            for sprite in background_sprite_group:
                if sprite.rect.y > height or sprite.rect.y < 0:
                    background_sprite_group.remove(sprite)
