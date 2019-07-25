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

#initialize some variables
newFire=None
collisionList=None
bugDirection=5
activeFire=pygame.sprite.Group()

pygame.init()
DISPLAYSURF= pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('shooting test')
DISPLAYSURF.fill(WHITE)

#bug1 moves back and forth
bug1=bug.Bug('bug.png', 0, 0)
bug1.update_rect()
DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))

smartBugs=pygame.sprite.Group()
smartBugs.add(bug1)

#bug3 is stationary so that bug2 can hit it
stationaryBugs=pygame.sprite.Group()
x=0
for i in range(0,10):
    bugTarget= bug.Bug('bug.png', 0+x, screenHeight-50)
    bugTarget.update_rect()
    DISPLAYSURF.blit(bugTarget.image, (bugTarget.x, bugTarget.y))
    stationaryBugs.add(bugTarget)
    x=x+50

count=0
while True:
    DISPLAYSURF.fill(BLACK)

    #draw/update stationary bugs group
    for bug in stationaryBugs:
        bug.update()
        DISPLAYSURF.blit(bug.image, (bug.x, bug.y))

    #display/update moving bug
    DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))
    newFire= bug1.update()
    if newFire:
        activeFire.add(newFire)
    #move bug this code will be deleted when bumpers added
    if bug1.rect.right >= screenWidth:
        bugDirection= -5
    if bug1.rect.left <= 0:
        bugDirection=5
    bug1.x = bug1.x + bugDirection

    #display and update bullets
    if activeFire:
        for bullet in activeFire:
            bullet.update()
            DISPLAYSURF.blit(bullet.image, (bullet.x, bullet.y))

    #check for collisions with bullets and bugs
    if activeFire:
        for bullet in activeFire:
            collisionList= pygame.sprite.spritecollide(bullet, stationaryBugs, True)
            if collisionList:
                activeFire.remove(bullet)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)