import pygame, sys
from pygame.locals import *

class Fire(pygame.sprite.Sprite):
    def __init__(self, shooter, direction):
        super().__init__()
        self.image = pygame.Surface([3, 5])
        self.image.fill((255,   0,   0))
        self.rect = self.image.get_rect()
        self.x=shooter.rect.center[0]
        self.y=shooter.rect.center[1]
        self.velocityX=0
        if (direction == "up"):
            self.velocityY=-5
        if (direction == "down"):
            self.velocityY=5

    def update(self):
        self.move()
        self.update_rect()
        
    def move(self):
        self.x=self.x + self.velocityX
        self.y=self.y + self.velocityY

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y
