import pygame
from network.client_socket import ClientSocket


class ClientGame:
    def __init__(self):
        self.client = ClientSocket()
        self.client.create_socket()
        self.client.connect_to_server()

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Client')
        self.send_packet_to_server = True
        self.state = 'lobby'

    def state_runnning(self):
        if self.state == 'lobby':
            self.lobby()

    def lobby(self):
        # 大廳，等待其他玩家加入
        self.screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.client.close()
                return


if __name__ == '__main__':
    client = ClientGame()
    client.game_init()
    while True:
        client.state_runnning()
        client.clock.tick(60)
