import pygame
from common.players import players
from entities.player import player
from network.client_socket import ClientSocket


class SparrowTenGame:
    def __init__(self):
        self.client = ClientSocket()
        self.client.create_socket()
        self.client.connect_to_server()

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.events = pygame.event.get()
        pygame.display.set_caption('Client')
        self.send_packet_to_server = True
        self.state = 'lobby'

    def update_events(self):
        self.events = pygame.event.get()
        player.key_pressed = self.collect_key_pressed()

    def collect_key_pressed(self):
        key_pressed = player.key_pressed
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                key_pressed.append(event.key)
            if event.type == pygame.KEYUP:
                key_pressed.remove(event.key)
        return key_pressed

    def state_runnning(self):
        if self.state == 'lobby':
            self.lobby()

    def lobby(self):
        # 大廳，等待其他玩家加入
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render('Lobby', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        self.screen.blit(text, text_rect)


if __name__ == '__main__':
    game = SparrowTenGame()
    game.game_init()
    game.client.t_update_players.start()
    while True:
        game.state_runnning()
        game.clock.tick(60)
        game.update_events()
        pygame.display.flip()
