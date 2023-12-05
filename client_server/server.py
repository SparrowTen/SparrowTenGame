import pygame
from common.global_variable import GV
from network.server_socket import ServerSocket


class SparrowTenServer:
    def __init__(self):
        self.server = ServerSocket()
        self.server.create_socket()
        # self.t_listen = threading.Thread(target=self.server.listen)
        # self.t_listen.start()

    def game_server_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0

    def run(self):
        while True:
            self.server.listen()
            self.dt = self.clock.tick(60) / 1000
            GV.set_tick(self.dt)
            print(GV.TICK)


if __name__ == '__main__':
    server = SparrowTenServer()
    server.game_server_init()
    server.run()
