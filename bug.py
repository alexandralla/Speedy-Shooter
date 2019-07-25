import pygame, sys
from pygame.locals import *
import random
import fire

class Bug(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        #pygame.sprite.Sprite.init(self)
        super().__init__()
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.move=None
        self.gridX = None 
        self.gridY = None

    def change_position(self, changeX, changeY):
        self.x= self.x + changeX
        self.y = self.y + changeY
        if (self.gridX is not None and self.gridY is not None):
            self.gridX= px_to_grid(self.x) 
            self.gridY= px_to_grid(self.y) 

    def update_rect(self):
         self.rect.x=self.x
         self.rect.y=self.y

    def update(self):
        global activeFire
        randomNum= random.randint(1,10)
        if randomNum == 1:
            newBullet= fire.Enemy_Fire(self)
            #activeFire.add(newBullet) 

    def bounce(self):
        pass

