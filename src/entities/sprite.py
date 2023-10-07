import pygame


class Sprite:
    def __init__(self, asset, start_x, start_y):
        super().__init__()
        self.pos = pygame.Vector2(start_x, start_y)

        self.asset = pygame.image.load(asset)
        self.rect = self.asset.get_rect()

        self.rect.center = (start_x, start_y)

        # 移動速度
        self.move_hsp = 100
        self.move_vsp = -300
        # 水平速度
        self.hsp = 0
        # 垂直速度
        self.vsp = 0

    def update(self):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.asset, self.rect)
