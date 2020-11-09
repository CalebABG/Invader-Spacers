import pygame
from math import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, display_width, display_height, dt):

        super(Player, self).__init__()

        self.display_width = display_width
        self.display_height = display_height

        self.initial_vel = 0.1  # Default value is 0.1
        self.time = float(dt / 300)
        self.movement = pi
        self.buoyancy = float(pi / 16 * 2.5)

        self.accelerate = (self.initial_vel + (self.movement * self.time))

        self.vx = 0
        self.vy = 0

        self.image = pygame.image.load("res/ship.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_vel(self):
        print("X: %s" % self.vx, "Y: %s" % self.vy)

    def change_speed(self, h_speed, v_speed):
        self.vx += h_speed
        self.vy += v_speed

    def death(self):
        pygame.sprite.Sprite.kill(self)

    def reg_shot(self, keys, alien_group, display_height, bullet_group):
        if keys[pygame.K_UP]:
            bullets = Bullet(alien_group)
            bullets.set_position(self.rect.centerx - 1, self.rect.y - 8)
            bullet_group.add(bullets)

            gravity = -20  # Default value is -15
            if bullets.v_speed == 0:
                bullets.v_speed += gravity

            for bullet in bullet_group:
                if bullet.rect.y < 0 or bullet.rect.y > display_height:
                    pygame.sprite.Sprite.kill(bullet)

    def death_ray_shot(self, keys, alien_group, display_height, bullet_group):
        if keys[pygame.K_UP]:
            bullets = Bullet(alien_group)
            bullets.set_position(self.rect.centerx - 1, self.rect.y - 8)
            bullet_group.add(bullets)

            gravity = -20  # Default value is -15
            if bullets.v_speed == 0:
                bullets.v_speed += gravity

            for bullet in bullet_group:
                if bullet.rect.y < 0 or bullet.rect.y > display_height:
                    pygame.sprite.Sprite.kill(bullet)

    def update(self, collidable, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.change_speed(-self.accelerate, 0)
        if keys[pygame.K_d]:
            self.change_speed(self.accelerate, 0)
        if keys[pygame.K_w]:
            self.change_speed(0, -self.accelerate)  # do not change signs i.e ( - or |x or y| )
        if keys[pygame.K_s]:
            self.change_speed(0, self.accelerate)

        self.vx *= 0.98729632121200
        self.vy *= 0.98722341212100

        # print("buoyancy rate: %f" % self.buoyancy)
        # print("acceleration rate: %f" % self.accelerate)
        # print("time: %f" % self.time)

        if self.rect.right > self.display_width:
            self.vx *= -.76
        elif self.rect.left < 0:
            self.vx *= -.76
        if self.rect.bottom > self.display_height:
            self.vy *= -.76
        elif self.rect.top < 0:
            self.vy *= -.76

        self.rect.x += self.vx

        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        for collided_object in collision_list:
            if self.vx > 0:
                # Right
                self.rect.right = collided_object.rect.left
            elif self.vx < 0:
                # LEFT
                self.rect.left = collided_object.rect.right

        self.rect.y += self.vy

        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        for collided_object in collision_list:
            if self.vy > 0:
                # Bottom
                self.rect.bottom = collided_object.rect.top
                self.vy = 0
            elif self.vy < 0:
                # Top
                self.rect.top = collided_object.rect.bottom
                self.vy = 0
