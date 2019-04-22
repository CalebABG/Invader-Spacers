import pygame
import sys
from Tools_class import *


class Score(pygame.sprite.Sprite):

    def __init__(self, start, displayw, displayh, window):
        super(Score, self).__init__()
