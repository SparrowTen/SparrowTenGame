import pygame
from entities.sprite import Sprite
from physics import Physics
from settings import SETTINGS


class Player(Sprite):
    def __init__(self, start_x, start_y):
        super().__init__(
            asset=SETTINGS.WORKDIR + "/assets/player_default.png",
            start_x=start_x,
            start_y=start_y,
        )
        self.physics = Physics()
        self.jump = True

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.jump:
                self.vsp = -300
        if keys[pygame.K_a]:
            self.hsp = -100
        if keys[pygame.K_d]:
            self.hsp = 100

        self.pos.y += self.vsp * dt
        self.pos.x += self.hsp * dt

        self.physics.apply_gravity(self, dt)
        self.physics.apply_friction(self, dt)

    def render(self, screen: pygame.Surface):
        screen.blit(self.asset, self.pos)
