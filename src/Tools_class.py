import pygame


class ScreenMessage(pygame.font.Font):

    def __init__(self, surface, msg, paint, font_size, x, y):
        self.fontSize = font_size

        font = pygame.font.SysFont("monospace", font_size)

        self.msg = msg
        self.color = paint

        self.x = x
        self.y = y

        surface.blit(font.render(msg, True, paint), [x, y])
