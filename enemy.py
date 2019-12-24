import pygame
from pygame.sprite import Sprite
from face import face

class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('images/shit.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 120
    def update(self):
        self.rect.y+=1
       
