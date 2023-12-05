import pygame
from common.global_variable import GV
from common.physics import apply_friction, apply_gravity, check_ground
from entities.sprite import Sprite
from settings import SETTINGS


class Player(Sprite):
    def __init__(self, start_x, start_y):
        super().__init__(
            asset=f'{SETTINGS.WORKDIR}/assets/player_default.png',
            start_x=start_x,
            start_y=start_y,
        )
        self.id = 0
        # 鳥的圖片大小為 64 x 64，但實際為 32 x 64
        self.rect = pygame.Rect(
            start_x,
            start_y,
            self.asset.get_width() / 2,
            self.asset.get_height(),
        )
        self.rect.center = (
            int(self.pos.x + self.rect.width),
            int(self.pos.y + self.rect.height / 2),
        )
        self.jump = True

        self.hsp: float = 0
        self.vsp: float = 0

        self.gravity = 9.8 * 50
        self.friction = 5 * 50

        self.key_pressed = []

    def move(self):
        for key in self.key_pressed:
            if key == pygame.K_SPACE:
                if self.jump:
                    self.vsp = -300
                    self.jump = False
            if key == pygame.K_a:
                self.hsp = -100
            if key == pygame.K_d:
                self.hsp = 100

        self.t_pos.y += self.vsp * GV.TICK
        self.t_pos.x += self.hsp * GV.TICK

    def update(self):
        self.move()
        self = apply_gravity(self)
        self = apply_friction(self)
        self = check_ground(self)

    def render(self, screen: pygame.Surface, pos_offset: pygame.Vector2() = pygame.Vector2(0, 0)):
        rect_offset = self.rect.copy()
        rect_offset.center = self.rect.center - pos_offset
        self.r_pos = self.pos - pos_offset
        screen.blit(self.asset, self.r_pos)

    def export_player_data(self):
        return {
            'id': self.id,
            'pos': self.pos,
            't_pos': self.t_pos,
            'rect': self.rect,
            'hsp': self.hsp,
            'vsp': self.vsp,
            'jump': self.jump,
            'gravity': self.gravity,
            'friction': self.friction,
            'key_pressed': self.key_pressed,
        }

    def import_play_data(self, player_data):
        self.id = player_data['id']
        self.pos = player_data['pos']
        self.t_pos = player_data['t_pos']
        self.rect = player_data['rect']
        self.hsp = player_data['hsp']
        self.vsp = player_data['vsp']
        self.jump = player_data['jump']
        self.gravity = player_data['gravity']
        self.friction = player_data['friction']


player = Player(start_x=SETTINGS.SCREEN[0] / 2, start_y=SETTINGS.SCREEN[1] / 2)
