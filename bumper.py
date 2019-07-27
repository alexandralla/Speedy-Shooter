import pygame, sys
from pygame.locals import *

class Bumper(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        print(width)
        print(height)
        self.image=pygame.Surface((width, height))
        self.image.fill((255,   255,   255))
        self.x=x
        self.y=y
        self.rect=self.image.get_rect()
        self.update_rect()

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y