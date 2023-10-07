import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, asset: str, start_x: int, start_y: int):
        """_summary_

        Args:
            asset (_type_): 實體的素材檔案路徑

            start_x (_type_): 起始位置的 x 座標

            start_y (_type_): 起始位置的 y 座標
        """

        super().__init__()
        self.pos = pygame.Vector2(start_x, start_y)
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

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        screen.blit(self.asset, self.pos)
