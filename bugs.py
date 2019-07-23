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
    def __init__(self, img, x, y, pxPerUnit):
        #pygame.sprite.Sprite.init(self)
        super().__init__()
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        #grid functions maybe change this to calculate the objects grid location based on its center.
        self.gridX = px_to_grid(self.x, pxPerUnit) 
        self.gridY = px_to_grid(self.y, pxPerUnit)
        self.rect = self.image.get_rect()
        
    def change_position(self, changeX, changeY, pxPerUnit):
        self.x= self.x + changeX
        self.y = self.y + changeY
        self.gridX= px_to_grid(self.x, pxPerUnit) 
        self.gridY= px_to_grid(self.y, pxPerUnit) 

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y

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

#bug1 moves back and forth
bug1=Bug('bug.png', 0, 0, pxPerUnit)
bug1.update_rect()
DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))


#bug2 moves down to colide with bug3
bug2= Bug('bug.png', 50, 0, pxPerUnit)
bug2.update_rect()
DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))

#bug3 is stationary so that bug2 can hit it
bug3= Bug('bug.png', 50, 200, pxPerUnit)
bug3.update_rect()
DISPLAYSURF.blit(bug3.image, (bug3.x, bug3.y))

movingBugs=pygame.sprite.Group()
movingBugs.add(bug2)

stationaryBugs=pygame.sprite.Group()
stationaryBugs.add(bug3)
#count=0
#for bug in stationaryBugs:
    #count=count +1
#print("stationary bug count", count)


#had to initialize the bug direction so that bug 1 can move back and forth
bugDirection=5
while True:
    DISPLAYSURF.fill(BLACK)
    
    #move_rect(rect1, "down", 10)
    #pygame.draw.rect(DISPLAYSURF, RED, rect1) 

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

    DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))
    #bug1.image.fill(WHITE)
    if bug1.x >= screenWidth:
        bugDirection= -5
        print(bug1.x)
        print(bug1.rect.right)
    if bug1.x < 0:
        bugDirection=5
    bug1.x = bug1.x + bugDirection
    bug1.update_rect()


    #draw moving bugs group
    for bug in movingBugs:
        DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))
        bug2.change_position(0, 1, pxPerUnit)
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