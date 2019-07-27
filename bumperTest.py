import pygame, sys
from pygame.locals import *
import bug

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
pygame.display.set_caption('bumper test')
DISPLAYSURF.fill(WHITE)

bumperTop=bug.Bumper('top', screenWidth, 1, 0, 0)
bumperBottom=bug.Bumper('bottom', screenWidth, 1, 0, screenHeight-1)
bumperRight=bug.Bumper('right', 1, screenHeight, screenWidth-1, 0)
bumperLeft=bug.Bumper('left', 1, screenHeight, 0, 0)

bumpers=pygame.sprite.Group()
bumpers.add(bumperTop)
bumpers.add(bumperRight)
bumpers.add(bumperBottom)
bumpers.add(bumperLeft)

bug=bug.Bug('bug.png', 50, 50, 5, 8)

while True:
    DISPLAYSURF.fill(BLACK)

    DISPLAYSURF.blit(bug.image, (bug.x, bug.y))
    bug.update()

    for bumper in bumpers:
        DISPLAYSURF.blit(bumper.image, (bumper.x, bumper.y))
    
    collisionList= pygame.sprite.spritecollide(bug, bumpers, False)
    if collisionList: 
        bug.bounce(collisionList)

   #for bug in movingBugs:
   #    bugOnBugCollisionList= pygame.sprite.spritecollide(bug, stationaryBugs, True)
   #    if bugOnBugCollisionList:
   #        movingBugs.remove(bug)    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)