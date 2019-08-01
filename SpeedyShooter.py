import pygame
import bug
pygame.init()

screenHeight=500
screenWidth=500
window = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('Speedy Shooter')
spaceShip = pygame.image.load('ship.png')

#make target bugs
stationaryBugs=pygame.sprite.Group()
x=0
for i in range(0,10):
    bugTarget = bug.Bug('bug.png', 0+x, 50)
    bugTarget.update_rect()
    window.blit(bugTarget.image, (bugTarget.x, bugTarget.y))
    stationaryBugs.add(bugTarget)
    x = x+50


#starting ship position coordinants
x = 220
y = 450
velocity = 10

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

activeBullets = []

gamePlay = True

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x + 18
        self.y = y - 10
        self .radius = 3
        self.velocity = 10
        self.color = RED

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


#function used for updating game actions and drawing
def updateWindow(x, y):

    window.blit(spaceShip, (x, y))
    for shots in activeBullets:
        shots.draw(window)
    pygame.display.update()


#while game is running
while gamePlay:

    pygame.time.wait(20)
    window.fill(BLACK)

    #check for game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamePlay = False

    # draw/update stationary bugs group
    for bug in stationaryBugs:
        bug.update()
        window.blit(bug.image, (bug.x, bug.y))

    #controls - arrow keys and space bar actions
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 13:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < 450:
        x += velocity

    if keys[pygame.K_UP] and y > 0:
        y -= velocity

    if keys[pygame.K_DOWN] and y < 450:
        y += velocity

    if keys[pygame.K_SPACE]:
        if len(activeBullets) < 20:
            newShot = bullet(x, y)
            activeBullets.append(newShot)

    #fire the bullets
    for shots in activeBullets:
        if shots.y < 500 and shots.y > 0:
            shots.y -= shots.velocity
        else:
            activeBullets.pop(activeBullets.index(shots))

    #redraw updates for this rotation
    updateWindow(x, y)

pygame.quit()