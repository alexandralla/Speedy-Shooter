import pygame, sys
from pygame.locals import *
import random
import bug
import fire
import explosion

#set up grid
screenHeight=400
screenWidth=300

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# frames per second setting
FPS = 10
fpsClock = pygame.time.Clock()

#initialize some variables
debris=pygame.sprite.Group()

pygame.init()
DISPLAYSURF= pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('shooting test')
DISPLAYSURF.fill(BLACK)

bug1=bug.Bug('bug.png', screenWidth/2, screenHeight/2, 0, 0)
newDebris=explosion.create_explosion(bug1)
for particle in newDebris:
    debris.add(particle)

while True:
    DISPLAYSURF.fill(BLACK)
    if debris:
        for particle in debris:
            #print('particle', count)
            DISPLAYSURF.blit(particle.image, (particle.x, particle.y))
            particle.update()
            if particle.velocityX == 0 and particle.velocityY == 0:
                debris.remove(particle)
                #print(particle.velocityX, " ", particle.velocityY)
                if len(debris.sprites()) == 0:
                    newDebris=explosion.create_explosion(particle)
                    for p in newDebris:
                        debris.add(p)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)