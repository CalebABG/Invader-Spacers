import pygame


class Particles(pygame.sprite.Sprite):
    """ First method to be called when the sprite (object) is created """
    """ Gives the sprite a color, width, height, vertical speed, and horizontal speed """

    def __init__(self, rgb, width, height):
        super(Particles, self).__init__()

        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect()

        self.image.fill(rgb)

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

        self.hspeed = 0
        self.vspeed = 0

    """ Method to set the position of the sprite """

    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    """ Method to update the particles """

    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
