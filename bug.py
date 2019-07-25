import pygame, sys
from pygame.locals import *
import random
import fire
import move as mv

class Bug(pygame.sprite.Sprite):
    def __init__(self, img, x, y, xVelocity=0, yVelocity=0, move=None):
        #pygame.sprite.Sprite.init(self)
        super().__init__()
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        self.xVelocity=xVelocity
        self.yVelocity=yVelocity
        self.rect = self.image.get_rect()
        if move is None:
            self.move=mv.simple_move
        else:
            self.move=move
        self.update_rect()
        #self.gridX = None 
        #self.gridY = None

#   def simple_move(self):
#       self.x= self.x + self.xVelocity
#       self.y = self.y + self.yVelocity

    def update_rect(self):
         self.rect.x=self.x
         self.rect.y=self.y

    def update(self):
        global activeFire
        self.move(self)
        self.update_rect()
        randomNum= random.randint(1,10)
        if randomNum == 1:
            newBullet= fire.Enemy_Fire(self)
            return newBullet
        return None

    def bounce(self):
        pass

