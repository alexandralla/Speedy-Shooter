import pygame, sys
from pygame.locals import *
import bumper

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

bumperTop=bumper.Bumper(screenWidth, 1, 0, 0)
bumperBottom=bumper.Bumper(screenWidth, 1, 0, screenHeight-1)
bumperRight=bumper.Bumper(1, screenHeight, screenWidth-1, 0)
bumperLeft=bumper.Bumper(1, screenHeight, 0, 0)

bumpers=pygame.sprite.Group()
bumpers.add(bumperTop)
bumpers.add(bumperRight)
bumpers.add(bumperBottom)
bumpers.add(bumperLeft)

while True:
    DISPLAYSURF.fill(BLACK)

    for bumper in bumpers:
        #bumper.update()
        DISPLAYSURF.blit(bumper.image, (bumper.x, bumper.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)