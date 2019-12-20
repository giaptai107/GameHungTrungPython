import pygame
class face:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #Load ảnh
        self.image = pygame.image.load('images/1.png')
        self.rect = self.image.get_rect()
        #Set vị trí
        self.rect.midbottom = self.screen_rect.midbottom

        # Direction
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x +=1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -=1
        
