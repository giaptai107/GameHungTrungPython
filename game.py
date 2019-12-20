import sys
import pygame
from face import face
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 700))
        self.bg_color = (100, 100, 100)
        self.face = face(self)
    


    def run_game(self):
        while True:
            self.check_event()
            self.face.update()
            self.update_game()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Check key pressed
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            # Check key released
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
                       

    def update_game(self):
        self.screen.fill(self.bg_color)
        self.face.blitme()
        pygame.display.flip()

    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.face.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.face.moving_left = True
        
    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.face.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.face.moving_left = False

        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
