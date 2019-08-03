import math
import pygame, sys
from pygame.locals import *
import random

class Explosion_Particle(pygame.sprite.Sprite):
    def __init__(self, ship, velocityX, velocityY):
        super().__init__()
        self.image = pygame.Surface([4, 4]) 
        self.image.fill((125,   125,   125))
        self.rect = self.image.get_rect()
        self.x=ship.rect.center[0]
        self.y=ship.rect.center[1]
        self.velocityX=velocityX 
        self.velocityY=velocityY

    def update(self):
        self.move()
        self.update_rect()
        self.decelerate()
        
    def move(self):
        self.x=self.x + self.velocityX
        self.y=self.y + self.velocityY

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y

    def decelerate(self, a=-1):
        acceleration=a
        oldVelocityX=self.velocityX        
        oldVelocityY=self.velocityY        
        
        if oldVelocityX ==0 and oldVelocityY ==0:
            self.velocityX = oldVelocityX       
            self.velocityY = oldVelocityY     
        elif oldVelocityX == 0 and 0-oldVelocityY<0:
            self.velocityY= math.ceil(oldVelocityY + a)
            #print('1', self.velocityX, self.velocityY)
        elif oldVelocityX == 0 and 0-oldVelocityY>0:
            self.velocityY= math.floor(oldVelocityY - a)
            #print('2', self.velocityX, self.velocityY)
        elif oldVelocityY == 0 and 0-oldVelocityX<0:
            self.velocityX= math.ceil(oldVelocityX + a)
            #print('3', self.velocityX, self.velocityY)
        elif oldVelocityY == 0 and 0-oldVelocityX>0:
            self.velocityX= math.floor(oldVelocityX - a)
            #print('4', self.velocityX, self.velocityY)
        else:            
            oldVelocity = math.sqrt(oldVelocityX * oldVelocityX  + oldVelocityY * oldVelocityY)
            newVelocity = oldVelocity + acceleration 
            angle = math.asin(oldVelocityY/oldVelocity)
            newXVelocity = math.cos(angle)/newVelocity
            newYVelocity = math.sin(angle)/newVelocity
            if(newXVelocity == 0 and newYVelocity ==0):
                self.velocityX = math.floor(newXVelocity)
                self.VelocityY = math.floor(newYVelocity)
            else:
                self.velocityX = 0
                self.VelocityY = 0

       #a=1
       #if random.randrange(0,4) == 0 and self.velocityX !=0:
       #    self.velocityX=self.velocityX - a
       #if random.randrange(0,4) == 0 and self.velocityY !=0:
       #    self.velocityY=self.velocityY - a

def create_explosion(ship, v=8):

    debris=[]
    for i in range(0,12):
        rad=i/2
        if random.randrange(0,3) == 0:
            rad=rad+.25
        debris.append(Explosion_Particle(ship,  (math.cos(rad)*v), (math.sin(rad)*v)))
    return debris