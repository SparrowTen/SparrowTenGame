import pygame

from settings import SETTINGS


class Sprite(pygame.sprite.Sprite):
    def __init__(self, asset: str, start_x: int, start_y: int):
        super().__init__()
        self.pos = pygame.Vector2(start_x, start_y)
        self.r_pos = pygame.Vector2(start_x, start_y)
        self.t_pos = pygame.Vector2(start_x, start_y)

        self.asset = pygame.image.load(asset)
        self.rect = self.asset.get_rect()

        self.rect.center = (start_x, start_y)

        # 移動速度
        self.move_hsp: float = 100
        self.move_vsp: float = -300

        # 速度
        self.hsp: float = 0
        self.vsp: float = 0

        self.jump = True

    def render(
        self,
        screen: pygame.Surface,
        pos_offset: pygame.Vector2() = pygame.Vector2(0, 0),
    ):
        rect_offset = self.rect.copy()
        rect_offset.center = self.rect.center - pos_offset
        self.r_pos = self.pos - pos_offset
        if SETTINGS.DEBUG:
            pygame.draw.rect(screen, (255, 0, 0), rect_offset)
        screen.blit(self.asset, self.r_pos)
