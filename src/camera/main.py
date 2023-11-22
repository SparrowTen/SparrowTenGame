import pygame

from entities.player import player
from map.scan_bmp_map import game_map
from settings import SETTINGS


class Camera:
    def __init__(self):
        self.x = SETTINGS.SCREEN[0] // 2
        self.y = SETTINGS.SCREEN[1] // 2
        self.range_x = 50
        self.range_y = 100
        self.scroll_speed = 0.5
        self.pos_offset = pygame.Vector2(0, 0)

    def check_player_in_camera(self, dt):
        if abs(player.r_pos.x - self.x) > self.range_x:
            self.pos_offset.x += (player.r_pos.x - self.x) * self.scroll_speed * dt
        if abs(player.r_pos.y - self.y) > self.range_y:
            self.pos_offset.y += (player.r_pos.y - self.y) * self.scroll_speed * dt

    def render(self, screen):
        player.render(screen, self.pos_offset)
        game_map.render(screen, self.pos_offset)


camera = Camera()
