import pygame
from common.global_variable import GV
from common.players import players
from network.server_socket import ServerSocket
from settings import SETTINGS


class SparrowTenServer:
    def __init__(self):
        self.server = ServerSocket()
        self.server.create_socket()
        # self.t_listen = threading.Thread(target=self.server.listen)
        # self.t_listen.start()

    def game_server_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self):
        self.server.listen()
        GV.TICK = self.clock.tick(60) / 1000

    def debug_info(self):
        if SETTINGS.DEBUG:
            print(f'TICK: {GV.TICK}')


if __name__ == '__main__':
    server = SparrowTenServer()
    server.game_server_init()
    while True:
        server.run()
        # server.debug_info()
