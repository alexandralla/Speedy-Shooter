import pygame, sys
from pygame.locals import *

def move_rect(rectObj, dir, speed):
    if dir == "down":
        rectObj.top=rectObj.top + speed
    elif dir =="up":
        rectObj.top=rectObj.top + speed
    elif dir == "left":
        rectObj.top=rectObj.left - speed
    else:
        rectObj.top=rectObj.left + speed

def move_img(x, y, dir, speed):
    if dir == "down":
        y = y + speed
    elif dir == "up":
        y = y + speed
    elif dir == "left":
        x = x - speed
    else:
        x = x + speed


def px_to_grid(length, pxPerUnit):
    return int(length/pxPerUnit)

class Bug(pygame.sprite.Sprite):
    def __init__(self, img, screenX, screenY, pxPerUnit):
        self.image = pygame.image.load(img)
        self.screenX = screenX
        self.screenY = screenY
        #grid functions maybe change this to calculate the objects grid location based on its center.
        self.gridX = px_to_grid(self.screenX, pxPerUnit) 
        self.gridY = px_to_grid(self.screenY, pxPerUnit)
        self.rect = self.image.get_rect()
        
    def change_position(self, changeX, changeY, pxPerUnit):
        self.screenX= self.screenX + changeX
        self.screenY = self.screenY + changeY
        self.gridX= px_to_grid(self.screenX, pxPerUnit) 
        self.gridY= px_to_grid(self.screenY, pxPerUnit) 

    def update_rect(self):
        self.rect.x=self.screenX
        self.rect.y=self.screenY

# -------------------------------------------------------
#                        main 
# -------------------------------------------------------

#set up grid
screenHeight=400
screenWidth=300
pxPerUnit=30

#GamePieceGridLocation

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
DISPLAYSURF= pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('Hello World!')
DISPLAYSURF.fill(WHITE)

#put  on screen
#rect1= pygame.Rect(0, 0, 20, 20)
#pygame.draw.rect(DISPLAYSURF, RED, rect1)

bug1=Bug('bug.png', 0, 0, pxPerUnit)
bug1.update_rect()
DISPLAYSURF.blit(bug1.image, (bug1.screenX, bug1.screenY))

#make bug as game piece
bug2= Bug('bug.png', 50, 0, pxPerUnit)
bug2.update_rect()
DISPLAYSURF.blit(bug2.image, (bug2.screenX, bug2.screenY))

#makle stationary bug to colide with
bug3= Bug('bug.png', 50, 200, pxPerUnit)
bug3.update_rect()
DISPLAYSURF.blit(bug3.image, (bug3.screenX, bug3.screenY))

# main game loop
bugDirection=1
while True:
    DISPLAYSURF.fill(BLACK)
    
    #move_rect(rect1, "down", 10)
    #pygame.draw.rect(DISPLAYSURF, RED, rect1) 
    
    
    DISPLAYSURF.blit(bug1.image, (bug1.screenX, bug1.screenY))
    #bug1.image.fill(WHITE)
    if bug1.screenX > screenWidth:
        bugDirection= -1
    if bug1.screenX < 0:
        bugDirection=1
    bug1.screenX = bug1.screenX + bugDirection
    bug1.update_rect()

    DISPLAYSURF.blit(bug2.image, (bug2.screenX, bug2.screenY))
    bug2.change_position(0, 1, pxPerUnit)
    bug2.update_rect()

    DISPLAYSURF.blit(bug3.image, (bug3.screenX, bug3.screenY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)