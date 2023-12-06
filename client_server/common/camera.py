import pygame
from common.global_variable import GV
from common.players import players
from entities.player import Player, player
from map.scan_map import map
from settings import SETTINGS


class Camera:
    def __init__(self):
        self.x = SETTINGS.SCREEN[0] // 2
        self.y = SETTINGS.SCREEN[1] // 2
        self.range_x = 50
        self.range_y = 100
        self.scroll_speed = 0.5
        self.pos_offset = pygame.Vector2(0, 0)

    def check_player_in_camera(self):
        if abs(player.r_pos.x - self.x) > self.range_x:
            self.pos_offset.x += (player.r_pos.x - self.x) * self.scroll_speed * GV.TICK
        if abs(player.r_pos.y - self.y) > self.range_y:
            self.pos_offset.y += (player.r_pos.y - self.y) * self.scroll_speed * GV.TICK

    def render(self, screen):
        player.render(screen, self.pos_offset)
        for player_id in players.players:
            other_player = players.players[player_id]
            other_player: Player
            other_player.render(screen, self.pos_offset)
        map.render(screen, self.pos_offset)


camera = Camera()
