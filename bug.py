import pygame, sys
from pygame.locals import *
import random
import fire
#import move as mv

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
            self.move=simple_move
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
            newBullet= fire.Fire(self, "down")
            return newBullet
        return None

    def bounce(self, bumpers):
        id=set()
        for bumper in bumpers:
            id.add(bumper.id)
        
        if 'left' in id or 'right' in id:
            self.xVelocity=self.xVelocity * -1

        if 'top' in id or 'bottom' in id:
            self.yVelocity=self.yVelocity * -1
        

class Bumper(pygame.sprite.Sprite):
    def __init__(self, id, width, height, x, y):
        super().__init__()
        self.id=id
        self.image=pygame.Surface((width, height))
        self.image.fill((255,   255,   255))
        self.x=x
        self.y=y
        self.rect=self.image.get_rect()
        self.update_rect()

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y

def simple_move(bug):
        bug.x= bug.x + bug.xVelocity
        bug.y = bug.y + bug.yVelocity