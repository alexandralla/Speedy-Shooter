import pygame
import bug
import fire
import ship
pygame.init()

screenHeight=500
screenWidth=500
window = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('Speedy Shooter')

playerFire=pygame.sprite.Group()
enemyFire=pygame.sprite.Group()
spaceShip = ship.Ship(screenWidth/2, screenHeight - 50)
bumpers=pygame.sprite.Group()
stationaryBugs = pygame.sprite.Group()

collisionList=None

bumperTop=bug.Bumper('top', screenWidth, 1, 0, 0)
bumperBottom=bug.Bumper('bottom', screenWidth, 1, 0, screenHeight-1)
bumperRight=bug.Bumper('right', 1, screenHeight, screenWidth-1, 0)
bumperLeft=bug.Bumper('left', 1, screenHeight, 0, 0)

bumpers.add(bumperTop)
bumpers.add(bumperRight)
bumpers.add(bumperBottom)
bumpers.add(bumperLeft)

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
YELLOW= (255, 255,   0)

velocity = 10
frame = 3

gamePlay = True
shipAlive = True
playerHealth = 480

def healthBar(health):

    if health > 350:
        healthColor = GREEN
    elif health > 150:
        healthColor = YELLOW
    elif health > 1:
        healthColor = RED
    else:
        healthColor = BLACK

    pygame.draw.rect(window, healthColor, (10, 10, health, 25))

#make target bugs
x=0
for i in range(0,10):
    bugTarget = bug.Bug('bug.png', 0 + x, 50, 5, 10)
    bugTarget.update_rect()
    window.blit(bugTarget.image, (bugTarget.x, bugTarget.y))
    stationaryBugs.add(bugTarget)
    x = x + 50

#while game is running
while gamePlay:

    pygame.time.wait(20)
    window.fill(BLACK)

    healthBar(playerHealth)

    #check for game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamePlay = False

    # draw/update stationary bugs group
    for bug in stationaryBugs:
        bug.update()
        window.blit(bug.image, (bug.x, bug.y))

    for bumper in bumpers:
        window.blit(bumper.image, (bumper.x, bumper.y))

    for bug in stationaryBugs:
        collisionList = pygame.sprite.spritecollide(bug, bumpers, False)
        if collisionList:
            bug.bounce(collisionList)

    if playerFire:
        for bullet in playerFire:
            bullet.update()
            window.blit(bullet.image, (bullet.x, bullet.y))

    #controls - arrow keys and space bar actions
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and spaceShip.x > 10:
        spaceShip.x -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_RIGHT] and spaceShip.x < 450:
        spaceShip.x += velocity
        spaceShip.update_rect()

    if keys[pygame.K_UP] and spaceShip.y > 10:
        spaceShip.y -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_DOWN] and spaceShip.y < 450:
        spaceShip.y += velocity
        spaceShip.update_rect()

    if keys[pygame.K_SPACE]:
        if shipAlive and frame % 3 == 0:
            newShot = fire.Fire(spaceShip, "up")
            playerFire.add(newShot)

#   check for collisions with bullets and bugs
    if playerFire:
        for bullet in playerFire:
            collisionList = pygame.sprite.spritecollide(bullet, stationaryBugs, True)
            if collisionList:
                playerFire.remove(bullet)

    shipOnBugCollisionList = pygame.sprite.spritecollide(spaceShip, stationaryBugs, True)
    if shipOnBugCollisionList:
        playerHealth = playerHealth - 50
        if playerHealth <= 0:
            shipAlive = False

    #redraw updates for this rotation
    if shipAlive:
        window.blit(spaceShip.image, (spaceShip.x, spaceShip.y))

    pygame.display.update()

    frame += 1

pygame.quit()