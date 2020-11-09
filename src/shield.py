import pygame
from pygame import gfxdraw


# Note to self: Create an arc sprite sheet for shield. Parent it above player (Ship)
# Shield color...


class Shield(pygame.sprite.Sprite):

    def __init__(self, player_sprite, enemies, shield_level):

        super(Shield, self).__init__()

        self.player = player_sprite

        self.enemies_group = enemies

        self.lifetime = 255

        if shield_level == 1:
            self.lifetime *= 2

        elif shield_level == 2:
            self.lifetime = 2048

        self.radius = 50

        self.image = pygame.Surface((108, 108))

        # pygame.gfxdraw.arc(self.image, self.radius, self.radius, self.radius, 180, 0, (0, 46, 184))
        pygame.gfxdraw.circle(self.image, self.radius, self.radius, self.radius, (0, 46, 184))

        self.image.set_colorkey((0, 0, 0))

        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()

    def get_lifetime(self):
        return self.lifetime

    def update(self):
        self.rect.center = self.player.rect.center

        if self.lifetime == 0:
            pygame.sprite.Sprite.kill(self)
        else:
            self.lifetime -= 1

        if self.get_lifetime() < 25:
            pygame.gfxdraw.circle(self.image, self.radius, self.radius, self.radius, (255, 0, 0))
            # pygame.gfxdraw.arc(self.image, self.radius, self.radius, self.radius, 180, 0, (255, 0, 0))

        pygame.sprite.spritecollide(self, self.enemies_group, True)
