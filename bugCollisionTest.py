import pygame, sys
from pygame.locals import *
import random
import bug
import fire

# -------------------------------------------------------
#                        main 
# -------------------------------------------------------

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
bug2= bug.Bug('bug.png', 50, 0)
bug2.update_rect()
DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))

#bug3 is stationary so that bug2 can hit it
bug3= bug.Bug('bug.png', 50, 200)
bug3.update_rect()
DISPLAYSURF.blit(bug3.image, (bug3.x, bug3.y))

movingBugs=pygame.sprite.Group()
movingBugs.add(bug2)

stationaryBugs=pygame.sprite.Group()
stationaryBugs.add(bug3)

#newFire=None

#had to initialize the bug direction so that bug 1 can move back and forth
bugDirection=5
while True:
    DISPLAYSURF.fill(BLACK)
    
    #check for collisions from two sprite groups
    #first argument and second is group, so might have to loop through sprites in one group to 
    #to check for collisions for list of sprites in another group
    #what setting does kill=True do?
    #answer: removes them from group, but would need to draw bugs on screen by groups so they are 
    #actually removed.
    for bug in movingBugs:
        bugOnBugCollisionList= pygame.sprite.spritecollide(bug, stationaryBugs, True)
        if bugOnBugCollisionList:
            movingBugs.remove(bug)    

    #draw moving bugs group
    for bug in movingBugs:
        DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))
        bug2.change_position(0, 1)
        bug2.update_rect()

    #dra stationary bugs group
    for bug in stationaryBugs:
        DISPLAYSURF.blit(bug.image, (bug.x, bug.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)