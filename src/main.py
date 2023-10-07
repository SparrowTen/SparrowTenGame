import pygame
from entities.player import Player
from settings import SETTINGS


class SparrowTenGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SETTINGS.SCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        # debug
        self.debug = True

    def run(self):
        player = Player(
            start_x=SETTINGS.SCREEN[0] / 2,
            start_y=SETTINGS.SCREEN[1] / 2,
        )

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(color="white")

            player.move(self.dt)
            # ground.check_on_ground(player)

            player.render(self.screen)

            if self.debug:
                self.screen.blit(
                    pygame.font.SysFont("Arial", 15).render(
                        f"FPS: {self.clock.get_fps()}", True, (100, 0, 0)
                    ),
                    (10, 10),
                )

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()


if __name__ == "__main__":
    game = SparrowTenGame()
    game.run()
