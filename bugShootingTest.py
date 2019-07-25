import pygame, sys
from pygame.locals import *
import random
import bug
import fire

#def move_rect(rectObj, dir, speed):
#    if dir == "down":
#        rectObj.top=rectObj.top + speed
#    elif dir =="up":
#        rectObj.top=rectObj.top + speed
#    elif dir == "left":
#        rectObj.top=rectObj.left - speed
#    else:
#        rectObj.top=rectObj.left + speed
#
#def move_img(x, y, dir, speed):
#    if dir == "down":
#        y = y + speed
#    elif dir == "up":
#        y = y + speed
#    elif dir == "left":
#        x = x - speed
#    else:
#        x = x + speed

#def px_to_grid(length):
#    return int(length/pxPerUnit)

#class Game_Object(pygame.sprite.Sprite):
#    def __init__(self):
#        super().__init__()
#






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

#fire=fire.Enemy_Fire(bug1)
#activeFire.add(fire)

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


    DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))
    #bug1.image.fill(WHITE)
    if bug1.rect.right >= screenWidth:
        bugDirection= -5
    if bug1.rect.left <= 0:
        bugDirection=5
    bug1.x = bug1.x + bugDirection
    bug1.update_rect()
    newFire= bug1.update()
    if newFire:
        activeFire.add(newFire)


    if activeFire:
        for bullet in activeFire:
            bullet.update()
            DISPLAYSURF.blit(bullet.image, (bullet.x, bullet.y))

    #dra stationary bugs group
    for bug in stationaryBugs:
        DISPLAYSURF.blit(bug.image, (bug.x, bug.y))

   #if activeFire:
   #    for bug in stationaryBugs:
   #        collisionList= pygame.sprite.spritecollide(bug, activeFire, True)
   #        if collisionList:
   #            stationaryBugs.remove(bug)    

    #probably want to have smallest list in inner loop
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