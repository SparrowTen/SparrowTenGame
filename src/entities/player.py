import pygame

from entities.sprite import Sprite
from physics import Physics
from settings import SETTINGS


class Player(Sprite):
    def __init__(self, start_x, start_y):
        super().__init__(
            asset=f'{SETTINGS.WORKDIR}/assets/player_default.png',
            start_x=start_x,
            start_y=start_y,
        )
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
        self.physics = Physics()
        self.jump = True

        self.hsp: float = 0
        self.vsp: float = 0

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.jump:
                self.vsp = -300
                self.jump = False
        if keys[pygame.K_a]:
            self.hsp = -100
        if keys[pygame.K_d]:
            self.hsp = 100

        self.t_pos.y += self.vsp * dt
        self.t_pos.x += self.hsp * dt

    def update(self, dt):
        self.move(dt)
        self.physics.apply_gravity(self, dt)
        self.physics.apply_friction(self, dt)
        self.physics.check_ground(self)


player = Player(
    start_x=SETTINGS.SCREEN[0] / 2,
    start_y=SETTINGS.SCREEN[1] / 2,
)
