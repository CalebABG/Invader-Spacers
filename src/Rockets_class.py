import pygame
from pygame.locals import *


class RocketAttatchments(pygame.sprite.Sprite):

    def __init__(self, display_width, display_height, collision_sprite_group):

        super(RocketAttatchments, self).__init__()

        self.displayw = display_width

        self.displayh = display_height

        self.collision_sprite_group = collision_sprite_group

        self.cool_down = 90

        self.lifetime = 200

        self.image = pygame.image.load("res/rocket.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.vx = 0
        self.vy = 0

    def set_position(self, x, y):

        self.rect.x = x
        self.rect.y = y

    def dead(self):
        try:
            pygame.sprite.Sprite.kill(self)
            return True
        except():
            return False

    def is_dead(self):
        if self.dead():
            return True
        else:
            return False

    def update(self):
        self.lifetime -= 1

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.y > self.displayh or self.rect.y < 0:
            self.dead()

        elif self.rect.y > self.displayw or self.rect.y < 0:
            self.dead()

        elif self.lifetime == 0:
            self.dead()

        hit_list = pygame.sprite.spritecollide(self, self.collision_sprite_group, True)

        # for x in hit_list:
        #     pygame.sprite.Sprite.kill(x)
        #     self.dead()
