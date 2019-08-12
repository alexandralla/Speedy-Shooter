import pygame
import bug as bg
import fire
import ship
import explosion


pygame.init()

# Load sound and background files
background = pygame.image.load('starlight.png')
explosion_sound = pygame.mixer.Sound('Kaboom2.wav')
blaster_sound = pygame.mixer.Sound('shoot1.wav')
bugBlaster_sound = pygame.mixer.Sound('bugShoot.wav')
beenHit_sound = pygame.mixer.Sound('collision.wav')

# Setup background music
pygame.mixer.music.load("drumBeats.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BRIGHT_RED = (150, 0, 0)
GREEN = (0, 190, 0)
DARK_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screenHeight = 500
screenWidth = 500
window = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('Speedy Shooter')

healthBarHeight = 25

playerFire = pygame.sprite.Group()
enemyFire = pygame.sprite.Group()
spaceShip = ship.Ship(screenWidth / 2, screenHeight - 50)
bumpers = pygame.sprite.Group()
stationaryBugs = pygame.sprite.Group()
debris = pygame.sprite.Group()

bumperTop = bg.Bumper('top', screenWidth, 1, 0, healthBarHeight + 25)
bumperBottom = bg.Bumper('bottom', screenWidth, 1, 0, screenHeight - 1)
bumperRight = bg.Bumper('right', 1, screenHeight, screenWidth - 1, 0)
bumperLeft = bg.Bumper('left', 1, screenHeight, 0, 0)

bumpers.add(bumperTop)
bumpers.add(bumperRight)
bumpers.add(bumperBottom)
bumpers.add(bumperLeft)

FPS = 30
fpsClock = pygame.time.Clock()


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


def button(text, x, y, width, height, brightHue, darkHue):
    mousePos = pygame.mouse.get_pos()
    pressButton = pygame.mouse.get_pressed()

    if ((x + width > mousePos[0] > x) and (y + height > mousePos[1] > y)):
        pygame.draw.rect(window, brightHue, (x, y, width, height))
        if pressButton[0] == 1:
            return True
    else:
        pygame.draw.rect(window, darkHue, (x, y, width, height))

    textFont = pygame.font.SysFont("Source Code Pro", 20)
    textSfc = textFont.render(text, True, YELLOW)
    textRect = textSfc.get_rect()
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    window.blit(textSfc, textRect)

    return False


def gameOverMenu():
    continueGame = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False

    pygame.mixer.pause()
    yesContinue = button("Continue", 100, 400, 110, 50, GREEN, DARK_GREEN)
    noExit = button("Quit", 300, 400, 110, 50, BRIGHT_RED, RED)

    if yesContinue:
        pygame.mixer.unpause()
        mainLoop()
    elif noExit:
        pygame.quit()
        quit()

    pygame.display.update()
    fpsClock.tick(FPS)


def mainLoop():
    collisionList = None
    levelCount = 1
    bugXVelocity = 3
    bugYVelovity = 1
    bugFiringPeriod = 80
    velocity = 10

    gamePlay = True
    shipAlive = True
    playerHealth = 400

    scoreFont = pygame.font.SysFont("Source Code Pro", 20)
    gameOverFont = pygame.font.SysFont("Source Code Pro", 30)
    score = 0
    scoreLabel = "SCORE: "

    while gamePlay:
        # pygame.time.wait(20)

        window.blit(background, (0, 0))

        healthBar(playerHealth)
        scoreLabel = scoreFont.render("SCORE: ", 1, WHITE)
        scoreDisplay = scoreFont.render(str(score), 1, WHITE)
        window.blit(scoreLabel, (415, 15))
        window.blit(scoreDisplay, (465, 15))

        # check for game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamePlay = False

        for bug in stationaryBugs:
            bullet = bug.update()
            window.blit(bug.image, (bug.x, bug.y))
            if bullet:
                pygame.mixer.Sound.play(bugBlaster_sound)
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

        # controls - arrow keys and space bar actions
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

        if spaceShip.hasFired == True and spaceShip.count % 4 == 0:
            pygame.mixer.Sound.play(blaster_sound)
            newShot = fire.Fire(spaceShip, "up")
            playerFire.add(newShot)
            spaceShip.hasFired = False

        #   check for collisions with bullets and bugs
        if playerFire:
            for bullet in playerFire:
                collisionList = pygame.sprite.spritecollide(bullet, stationaryBugs, True)
                if collisionList:
                    playerFire.remove(bullet)
                    pygame.mixer.Sound.play(beenHit_sound)
                    newDebris = explosion.create_explosion(bullet)
                    for particle in newDebris:
                        debris.add(particle)
                    score += 1

        if enemyFire and shipAlive:
            # for bullet in enemyFire:
            collisionList = pygame.sprite.spritecollide(spaceShip, enemyFire, True)
            if collisionList:
                pygame.mixer.Sound.play(explosion_sound)
                newDebris = explosion.create_explosion(spaceShip)
                for particle in newDebris:
                    debris.add(particle)
                score += 1

                playerHealth = playerHealth - 25

                if playerHealth <= 0:
                    shipAlive = False

        if shipAlive:
            shipOnBugCollisionList = pygame.sprite.spritecollide(spaceShip, stationaryBugs, True)
            if shipOnBugCollisionList:
                newDebris=explosion.create_explosion(spaceShip)
                for p in newDebris:
                    debris.add(p)
                pygame.mixer.Sound.play(explosion_sound)
                playerHealth = playerHealth - 25
            if playerHealth <= 0:
                shipAlive = False

        for particle in debris:
            if particle.velocityX == 0 and particle.velocityY == 0:
                debris.remove(particle)

        if len(stationaryBugs) <= 3:
            levelCount += 1
            # make target bugs
            bugXVelocity += 1 * -1
            bugYVelovity += 1
            bugFiringPeriod -= 4
            x = 0

            for i in range(0, 10):
                bugTarget = None
                bugTarget = bg.Bug('aliensprite2.png', 0 + x, 50, bugXVelocity, bugYVelovity, bugFiringPeriod)
                #   bugTarget.update_rect()
                window.blit(bugTarget.image, (bugTarget.x, bugTarget.y))
                stationaryBugs.add(bugTarget)
                x = x + 50

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

            gameOverMenu()

        pygame.display.update()
        fpsClock.tick(FPS)


mainLoop()
pygame.quit()
quit()