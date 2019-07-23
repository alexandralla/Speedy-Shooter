import pygame, sys
from pygame.locals import *
import random

activeFire= None

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


def px_to_grid(length):
    return int(length/pxPerUnit)

class Bug(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        #pygame.sprite.Sprite.init(self)
        super().__init__()
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.gridX = None 
        self.gridY = None

#   def __init__(self, img, x, y):
#       #pygame.sprite.Sprite.init(self)
#       super().__init__()
#       self.image = pygame.image.load(img)
#       self.x = x
#       self.y = y
#       #grid functions maybe change this to calculate the objects grid location based on its center.
#       self.gridX = px_to_grid(self.x) 
#       self.gridY = px_to_grid(self.y)
#       self.rect = self.image.get_rect()

    def change_position(self, changeX, changeY):
        self.x= self.x + changeX
        self.y = self.y + changeY
        if (self.gridX is not None and self.gridY is not None):
            self.gridX= px_to_grid(self.x) 
            self.gridY= px_to_grid(self.y) 

    def update_rect(self):
        self.rect.x=self.x
        self.rect.y=self.y

    def update(self):
        global activeFire
        randomNum= random.randint(1,10)
        if randomNum == 1:
            newBullet= Enemy_Fire(self)
            activeFire.add(newBullet) 

class Enemy_Fire(pygame.sprite.Sprite):
    def __init__(self, shooter):
        super().__init__()
        self.image = pygame.Surface([3, 10]) 
        self.image.fill((255,   0,   0))
        self.rect = self.image.get_rect()
        self.x=shooter.rect.center[0]
        self.y=shooter.rect.center[1]
        self.velocityX=0 
        self.velocityY=5
    
    def update(self):
        self.move()

    def move(self):
        self.x=self.x + self.velocityX
        self.y=self.y + self.velocityY


        

# -------------------------------------------------------
#                        main 
# -------------------------------------------------------
#global activeFire

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
DISPLAYSURF= pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Hello World!')
DISPLAYSURF.fill(WHITE)

#put  on screen
#rect1= pygame.Rect(0, 0, 20, 20)
#pygame.draw.rect(DISPLAYSURF, RED, rect1)

#bug1 moves back and forth
bug1=Bug('bug.png', 0, 0)
bug1.update_rect()
DISPLAYSURF.blit(bug1.image, (bug1.x, bug1.y))

smartBugs=pygame.sprite.Group()
smartBugs.add(bug1)

fire=Enemy_Fire(bug1)
activeFire=pygame.sprite.Group()
activeFire.add(fire)

#bug2 moves down to colide with bug3
bug2= Bug('bug.png', 50, 0)
bug2.update_rect()
DISPLAYSURF.blit(bug2.image, (bug2.x, bug2.y))

#bug3 is stationary so that bug2 can hit it
bug3= Bug('bug.png', 50, 200)
bug3.update_rect()
DISPLAYSURF.blit(bug3.image, (bug3.x, bug3.y))

movingBugs=pygame.sprite.Group()
movingBugs.add(bug2)

stationaryBugs=pygame.sprite.Group()
stationaryBugs.add(bug3)


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
    if bug1.rect.right >= screenWidth:
        bugDirection= -5
    if bug1.rect.left <= 0:
        bugDirection=5
    bug1.x = bug1.x + bugDirection
    bug1.update_rect()
    bug1.update()

    count=0
    for bullet in activeFire:
        bullet.update()
        DISPLAYSURF.blit(bullet.image, (bullet.x, bullet.y))
    #print(count)

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