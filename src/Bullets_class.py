import pygame
from Player_class import *
from Explosions_class import *


class Bullet(pygame.sprite.Sprite):

    def __init__(self, sprite_group):

        super(Bullet, self).__init__()

        self.sprite_groups = sprite_group

        self.lifetime = 50

        self.image = pygame.image.load("res/bullet.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.hspeed = 0
        self.vspeed = 0

    def set_position(self, x, y):

        self.rect.x = x
        self.rect.y = y

    def update(self):

        self.lifetime -= 1

        if self.lifetime == 0:
            pygame.sprite.Sprite.kill(self)

        self.rect.x += self.hspeed
        self.rect.y += self.vspeed

        hit_list = pygame.sprite.spritecollide(self, self.sprite_groups, True)

        for x in self.sprite_groups:
            for x in hit_list:
                pygame.sprite.Sprite.kill(x)
                pygame.sprite.Sprite.kill(self)
