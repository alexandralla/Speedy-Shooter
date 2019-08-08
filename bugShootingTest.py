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
#FPS = 30
FPS = 10
fpsClock = pygame.time.Clock()

#initialize some variables
newFire=None
collisionList=None
activeFire=pygame.sprite.Group()
debris=pygame.sprite.Group()

pygame.init()
DISPLAYSURF= pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('shooting test')
DISPLAYSURF.fill(WHITE)

#make bumpers
bumperTop=bug.Bumper('top', screenWidth, 1, 0, 0)
bumperBottom=bug.Bumper('bottom', screenWidth, 1, 0, screenHeight-1)
bumperRight=bug.Bumper('right', 1, screenHeight, screenWidth-1, 0)
bumperLeft=bug.Bumper('left', 1, screenHeight, 0, 0)
bumpers=pygame.sprite.Group()
bumpers.add(bumperTop)
bumpers.add(bumperRight)
bumpers.add(bumperBottom)
bumpers.add(bumperLeft)

bug1=bug.Bug('bug.png', 1, 1, 5, 0)
DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))
smartBugs=pygame.sprite.Group()
smartBugs.add(bug1)

#make target bugs
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

    #check for collisions with bumpers
    collisionList= pygame.sprite.spritecollide(bug1, bumpers, False)
    if collisionList: 
        bug1.bounce(collisionList)
        
    #draw/update stationary bugs group
    for bug in stationaryBugs:
        bug.update()
        DISPLAYSURF.blit(bug.image, (bug.x, bug.y))

    #display/update moving bug
    DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))
    newFire= bug1.update()
    if newFire:
        activeFire.add(newFire)

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
                newDebris=explosion.create_explosion(bullet)
                for particle in newDebris:
                    debris.add(particle)
                activeFire.remove(bullet)

    for particle in debris:
        if particle.velocityX ==0 and particle.velocityY == 0:
            debris.remove(particle)
        else:
            DISPLAYSURF.blit(particle.image, (particle.x, particle.y))
            particle.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)