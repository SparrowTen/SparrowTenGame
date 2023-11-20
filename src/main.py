import pygame

from camera.main import camera
from entities.player import player
from map.scan_bmp_map import game_map
from settings import SETTINGS


class SparrowTenGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SETTINGS.SCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            # update
            player.update(self.dt)

            # render
            camera.check_player_in_camera(self.dt)
            camera.render(self.screen)
            # game_map.render(self.screen)
            # player.render(self.screen)

            # debug
            if SETTINGS.DEBUG:
                self.screen.blit(
                    pygame.font.SysFont('Arial', 15).render(
                        f'FPS: {self.clock.get_fps()}', True, (100, 0, 0)
                    ),
                    (10, 10),
                )
                self.screen.blit(
                    pygame.font.SysFont('Arial', 15).render(
                        f'Camera offset: {camera.pos_offset.x}, {camera.pos_offset.y}',
                        True,
                        (100, 0, 0),
                    ),
                    (10, 50),
                )
                self.screen.blit(
                    pygame.font.SysFont('Arial', 15).render(
                        f'Player rect center: {player.rect.center}',
                        True,
                        (100, 0, 0),
                    ),
                    (10, 30),
                )
                self.screen.blit(
                    pygame.font.SysFont('Arial', 15).render(
                        f'Player hsp: {player.hsp}', True, (100, 0, 0)
                    ),
                    (10, 70),
                )
                self.screen.blit(
                    pygame.font.SysFont('Arial', 15).render(
                        f'Player vsp: {player.vsp}', True, (100, 0, 0)
                    ),
                    (10, 90),
                )

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()


if __name__ == '__main__':
    game = SparrowTenGame()
    game.run()
