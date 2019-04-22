import pygame

GRAVITY = 9.81


class Explosion(pygame.sprite.Sprite):
    gravity = True

    def __init__(self, pos):
        super(Explosion, self).__init__()
