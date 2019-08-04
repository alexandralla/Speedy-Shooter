import math
import pygame, sys
from pygame.locals import *
import random

class Explosion_Particle(pygame.sprite.Sprite):
    def __init__(self, ship, velocityX, velocityY, color=(125, 125, 125)):
        super().__init__()
        self.image = pygame.Surface([4, 4]) 
        self.image.fill(color)
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
        self.x=self.x + int(self.velocityX)
        self.y=self.y + int(self.velocityY)

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y

    def decelerate(self, a=-1):
        print(self.velocityX, ', ', self.velocityY)
        acceleration=a
        oldVelocityX=self.velocityX        
        oldVelocityY=self.velocityY        
        #particle is not moving  
        if oldVelocityX == 0 and oldVelocityY == 0:
            self.velocityX = oldVelocityX       
            self.velocityY = oldVelocityY     
        #moving down
        elif oldVelocityX == 0 and 0-oldVelocityY<0:
            self.velocityY= math.floor(oldVelocityY + a)
        #moving up
        elif oldVelocityX == 0 and 0-oldVelocityY>0:
            self.velocityY= math.ceil(oldVelocityY - a)
        #moving right
        elif oldVelocityY == 0 and 0-oldVelocityX<0:
            self.velocityX= math.floor(oldVelocityX + a)
        #moving left
        elif oldVelocityY == 0 and 0-oldVelocityX>0:
            self.velocityX= math.ceil(oldVelocityX - a)
        else:            
            oldVelocity = math.sqrt((oldVelocityX * oldVelocityX)  + (oldVelocityY * oldVelocityY))
            newVelocity = oldVelocity + acceleration 
            
            absVelocityX=abs(oldVelocityX)
            absVelocityY=abs(oldVelocityY)

            angle = math.asin(absVelocityY/oldVelocity)
            #angle = math.acos(oldVelocityX/oldVelocity)
            #angle = math.atan(oldVelocityY/oldVelocityX)

            newXVelocity = math.cos(angle)*newVelocity
            newYVelocity = math.sin(angle)*newVelocity

            accX=absVelocityX - newXVelocity
            accY=absVelocityY - newYVelocity
            print('abs change in velocity: ', accX, accY)

            randX=random.randrange(0,3)
            randY=random.randrange(0,3)
            if randX ==0:
                accX=0
            if randY ==0:
                accY=0
            #moving down
            if 0-oldVelocityY<0:
                self.velocityY= math.floor(self.velocityY-accY)
            #moving up
            else:
                self.velocityY= math.ceil(self.velocityY+accY)
            #moving right
            if 0-oldVelocityX<0:
                self.velocityX= math.floor(self.velocityX - accX)
            #moving left
            else:
                self.velocityX= math.ceil(self.velocityX + accX)

        print(self.velocityX,', ', self.velocityY)


def create_explosion(ship, v=6):
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    debris=[]
    for i in range(0,12):
        rad=i/2

        if rad>=0 and rad<(math.pi/2):
            color=WHITE
        elif rad >= (math.pi/2) and rad < math.pi:
            color=RED
        elif rad>=(math.pi) and rad<((3 * math.pi)/2):
            color=GREEN
        elif rad >= ((3 * math.pi)/2) and rad < (math.pi*2):
            color=BLUE
        else:
            color=BLACK
        debris.append(Explosion_Particle(ship,  (math.cos(rad)*v), (math.sin(rad)*v), (125, 125, 125)))
    return debris