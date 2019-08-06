import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, shipImage = 'ship.png'):
        #pygame.sprite.Sprite.init(self)
        super().__init__()
        self.image = pygame.image.load(shipImage)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.update_rect()
        self.count = 0
        self.hasFired = False


    def update_rect(self):
         self.rect.x=self.x
         self.rect.y=self.y