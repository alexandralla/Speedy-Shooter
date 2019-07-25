import pygame, sys
from pygame.locals import *

class Bumper(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.image=pygame.Surface(width, height)
        self.image.fill((255,   255,   255))
        self.rect=self.image.get_rect()