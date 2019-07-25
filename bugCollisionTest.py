import pygame, sys
from pygame.locals import *
import random
import bug
import fire

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
FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF= pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('bug collision test')
DISPLAYSURF.fill(WHITE)

#bug2 moves down to colide with bug3
bug2= bug.Bug('bug.png', 50, 0, 0, 5)
DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))

#bug3 is stationary so that bug2 can hit it
bug3= bug.Bug('bug.png', 50, 200)
DISPLAYSURF.blit(bug3.image, (bug3.x, bug3.y))

movingBugs=pygame.sprite.Group()
movingBugs.add(bug2)

stationaryBugs=pygame.sprite.Group()
stationaryBugs.add(bug3)

while True:
    DISPLAYSURF.fill(BLACK)
    
    for bug in movingBugs:
        bug.update()
        DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))

    for bug in stationaryBugs:
        bug.update()
        DISPLAYSURF.blit(bug.image, (bug.x, bug.y))

    for bug in movingBugs:
        bugOnBugCollisionList= pygame.sprite.spritecollide(bug, stationaryBugs, True)
        if bugOnBugCollisionList:
            movingBugs.remove(bug)    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)