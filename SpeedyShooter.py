import pygame
import bug
import fire
import ship
import explosion
pygame.init()

screenHeight=500
screenWidth=500
window = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('Speedy Shooter')

FPS = 30
fpsClock =pygame.time.Clock()

playerFire=pygame.sprite.Group()
enemyFire=pygame.sprite.Group()
spaceShip = ship.Ship(screenWidth/2, screenHeight - 50)
bumpers=pygame.sprite.Group()
stationaryBugs = pygame.sprite.Group()
debris = pygame.sprite.Group()

collisionList=None
healthBarHeight = 25

bumperTop=bug.Bumper('top', screenWidth, 1, 0, healthBarHeight+25)
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

gamePlay = True
shipAlive = True
playerHealth = 400


scoreFont = pygame.font.SysFont("Source Code Pro", 20)
gameOverFont = pygame.font.SysFont("Source Code Pro", 30)
score = 0
scoreLabel = "SCORE: "

def healthBar(health):

    if health > 300:
        healthColor = GREEN
    elif health > 150:
        healthColor = YELLOW
    elif health > 50:
        healthColor = RED
    else:
        healthColor = BLACK

    pygame.draw.rect(window, healthColor, (10, 10, health, healthBarHeight))

#make target bugs
x=0
for i in range(0,10):
    bugTarget = bug.Bug('bug.png', 0 + x, 50, 5, 1)
    bugTarget.update_rect()
    window.blit(bugTarget.image, (bugTarget.x, bugTarget.y))
    stationaryBugs.add(bugTarget)
    x = x + 50


#while game is running
while gamePlay:

    #pygame.time.wait(20)
    window.fill(BLACK)

    healthBar(playerHealth)
    scoreLabel = scoreFont.render("SCORE: ", 1, WHITE)
    scoreDisplay = scoreFont.render(str(score), 1, WHITE)

    #check for game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamePlay = False

    for bug in stationaryBugs:
        bullet = bug.update()
        window.blit(bug.image, (bug.x, bug.y))
        if bullet:
            enemyFire.add(bullet)

    for bullet in enemyFire:
        bullet.update()
        window.blit(bullet.image, (bullet.x, bullet.y))

    debris.update()
    debris.draw(window)

    for bug in stationaryBugs:
        collisionList = pygame.sprite.spritecollide(bug, bumpers, False)
        if collisionList:
            bug.bounce(collisionList)


    if playerFire:
        for bullet in playerFire:
            bullet.update()
            bumperCollision = pygame.sprite.spritecollide(bullet, bumpers, False)
            if bumperCollision:
                playerFire.remove(bullet)
            window.blit(bullet.image, (bullet.x, bullet.y))

    #controls - arrow keys and space bar actions
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and spaceShip.x > 10:
        spaceShip.x -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_RIGHT] and spaceShip.x < 450:
        spaceShip.x += velocity
        spaceShip.update_rect()

    if keys[pygame.K_UP] and spaceShip.y > 50:
        spaceShip.y -= velocity
        spaceShip.update_rect()

    if keys[pygame.K_DOWN] and spaceShip.y < 450:
        spaceShip.y += velocity
        spaceShip.update_rect()

    if keys[pygame.K_SPACE]:
        if shipAlive:
            spaceShip.hasFired = True

    if spaceShip.hasFired == True and spaceShip.count % 5 == 0:
        newShot = fire.Fire(spaceShip, "up")
        playerFire.add(newShot)
        spaceShip.hasFired = False

#   check for collisions with bullets and bugs
    if playerFire:
        for bullet in playerFire:
            collisionList = pygame.sprite.spritecollide(bullet, stationaryBugs, True)
            if collisionList:
                playerFire.remove(bullet)
                newDebris = explosion.create_explosion(bullet)
                for particle in newDebris:
                    debris.add(particle)
                score += 1

    if enemyFire and shipAlive:
       # for bullet in enemyFire:
        collisionList = pygame.sprite.spritecollide(spaceShip, enemyFire, True)
        if collisionList:
            newDebris = explosion.create_explosion(spaceShip)
            for particle in newDebris:
                debris.add(particle)
            score += 1

            playerHealth = playerHealth - 50

            if playerHealth <= 0:
                shipAlive = False

    if shipAlive:
        shipOnBugCollisionList = pygame.sprite.spritecollide(spaceShip, stationaryBugs, True)
        if shipOnBugCollisionList:
            playerHealth = playerHealth - 100
        if playerHealth <= 0:
            shipAlive = False

    for particle in debris:
        if particle.velocityX ==0 and particle.velocityY == 0:
            debris.remove(particle)

    if shipAlive:
        window.blit(spaceShip.image, (spaceShip.x, spaceShip.y))
        spaceShip.count += 1
    else:
        gameOver = gameOverFont.render("GAME OVER! ", 1, WHITE)
        finalScoreLabel = gameOverFont.render("FINAL SCORE: ", 1, WHITE)
        finalScoreDisplay = gameOverFont.render(str(score), 1, WHITE)
        window.blit(gameOver, (180, 250))
        window.blit(finalScoreLabel, (160, 280))
        window.blit(finalScoreDisplay, (310, 280))

    window.blit(scoreLabel, (415, 15))
    window.blit(scoreDisplay, (465, 15))
    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()