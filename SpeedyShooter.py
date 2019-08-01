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

collisionList=None

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


gamePlay = True

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

    if playerFire:
        for bullet in playerFire:
            bullet.update()
            window.blit(bullet.image, (bullet.x, bullet.y))

    #controls - arrow keys and space bar actions
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 13:
        spaceShip.x -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_RIGHT] and x < 450:
        spaceShip.x += velocity
        spaceShip.update_rect()

    if keys[pygame.K_UP] and y > 0:
        spaceShip.y -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_DOWN] and y < 450:
        spaceShip.y += velocity
        spaceShip.update_rect()

    if keys[pygame.K_SPACE]:
        if len(playerFire) < 20:
            newShot = fire.Fire(spaceShip, "up")
            playerFire.add(newShot)

#   check for collisions with bullets and bugs
    if playerFire:
        for bullet in playerFire:
            collisionList = pygame.sprite.spritecollide(bullet, stationaryBugs, True)
            if collisionList:
                playerFire.remove(bullet)

    #redraw updates for this rotation
    window.blit(spaceShip.image, (spaceShip.x, spaceShip.y))
    pygame.display.update()

pygame.quit()