import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Speedy Shooter')
spaceShip = pygame.image.load('ship.png')

x = 220
y = 450
velocity = 10

run = True

def ship(x, y):
    window.blit(spaceShip, (x, y))

while run:

    pygame.time.delay(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 13:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < 450:
        x += velocity

    if keys[pygame.K_UP] and y > 0:
        y -= velocity

    if keys[pygame.K_DOWN] and y < 450:
        y += velocity

    #if keys[pygame.K_SPACE]:


    window.fill((0, 0, 0))

    ship(x, y)
    pygame.display.update()

pygame.quit()