import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Speedy Shooter')
spaceShip = pygame.image.load('ship.png')

#starting ship position coordinants
x = 220
y = 450
velocity = 10

RED = (255, 0, 0)
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

    window.fill((0, 0, 0))
    ship(x, y)
    for shots in activeBullets:
        shots.draw(window)
    pygame.display.update()


def ship(x, y):
    window.blit(spaceShip, (x, y))

#while game is running
while gamePlay:

    #check for game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamePlay = False

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