import pygame


class MoveObject:
    def __init__(self):
        self.pos = pygame.Vector2(0, 0)
        self.velocity_x = 0
        self.velocity_y = 0