import pygame
from entities.player import Player
from physics import Physics
from settings import SETTINGS

class SparrowTen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SETTINGS.SCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        
    def run(self):
        player = Player(pygame.Vector2(100, 100))
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(color="white")

            player.move(self.dt)
            player.render(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()

if __name__ == "__main__":
    game = SparrowTen()
    game.run()