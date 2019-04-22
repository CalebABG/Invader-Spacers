from Explosions_class import *


class Aliens(pygame.sprite.Sprite):

    def __init__(self, width, height, player, player_sprite_group):
        super(Aliens, self).__init__()

        self.player_sprite = player

        self.player_group = player_sprite_group

        self.image = pygame.image.load("res/alien.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

        self.displayWidth = width
        self.displayHeight = height

        self.vx = 0
        self.vy = 0

    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def change_speed(self, vx, vy):
        self.vx += vx
        self.vy += vy

    def death(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.y > self.displayHeight:
            self.death()

        hit_list = pygame.sprite.spritecollide(self, self.player_group, True)
