import sys

import pygame
from common.camera import camera
from common.global_variable import GV
from entities.player import player
from network.client_socket import ClientSocket
from settings import SETTINGS


class SparrowTenGame:
    def __init__(self, player_name):
        self.client = ClientSocket()
        self.client.create_socket()
        self.client.connect_to_server()
        self.player_name = player_name

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SETTINGS.SCREEN)
        self.events = pygame.event.get()
        pygame.display.set_caption(f'player {self.player_name}')
        self.send_packet_to_server = True

    def update_events(self):
        self.events = pygame.event.get()
        player.set_key_pressed(self.collect_key_pressed())

    def collect_key_pressed(self):
        key_pressed = player.get_key_pressed()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                key_pressed.append(event.key)
            if event.type == pygame.KEYUP:
                if event.key in key_pressed:
                    key_pressed.remove(event.key)
        return key_pressed

    def state_runnning(self):
        if GV.STATE == 'lobby':
            self.lobby()

    def lobby(self):
        # 大廳，等待其他玩家加入
        self.screen.fill((255, 255, 255))
        # font = pygame.font.Font(None, 36)
        # text = font.render('Lobby', True, (0, 0, 0))
        # text_rect = text.get_rect()
        # text_rect.center = (400, 300)
        # self.screen.blit(text, text_rect)
        camera.check_player_in_camera()
        camera.render(self.screen)

    def debug_info(self):
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
            self.screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    f'Player key pressed: {player.key_pressed}', True, (100, 0, 0)
                ),
                (10, 110),
            )


if __name__ == '__main__':
    game = SparrowTenGame()
    game.game_init(sys.argv[1])
    game.client.t_update_player_and_get_data.start()
    player.id = game.client.client.getsockname()[1]
    while True:
        game.state_runnning()
        game.clock.tick(60)
        game.update_events()
        game.debug_info()
        pygame.display.flip()
        GV.TICK = game.clock.tick(60) / 1000
