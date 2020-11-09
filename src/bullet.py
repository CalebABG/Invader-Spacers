import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, sprite_group):
        super(Bullet, self).__init__()

        self.sprite_groups = sprite_group

        self.lifetime = 50

        self.image = pygame.image.load("res/bullet.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.h_speed = 0
        self.v_speed = 0

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.lifetime -= 1

        if self.lifetime == 0:
            pygame.sprite.Sprite.kill(self)

        self.rect.x += self.h_speed
        self.rect.y += self.v_speed

        pygame.sprite.spritecollide(self, self.sprite_groups, True)
