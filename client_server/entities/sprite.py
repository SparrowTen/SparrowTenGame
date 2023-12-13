import pygame
from settings import SETTINGS


class Sprite(pygame.sprite.Sprite):
    def __init__(self, asset: str, start_x: int, start_y: int):
        super().__init__()
        self.pos = pygame.Vector2(start_x, start_y)  # 現在座標
        self.t_pos = pygame.Vector2(start_x, start_y)  # 目標座標
        self.r_pos = pygame.Vector2(start_x, start_y)  # camera 偏移後座標

        self.asset = pygame.image.load(asset)
        self.rect = self.asset.get_rect()

        self.rect.center = (
            int(self.pos.x + self.rect.width / 2),
            int(self.pos.y + self.rect.height / 2),
        )

        # 移動速度
        self.move_hsp: float
        self.move_vsp: float

        # 速度
        self.hsp: float
        self.vsp: float

        # 重力和摩擦力
        self.gravity = 9.8 * 50
        self.friction = 5 * 50

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
