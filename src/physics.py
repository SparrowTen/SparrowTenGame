import numpy as np
from entities.sprite import Sprite


class Physics:
    def __init__(self, gravity=9.8, friction=5.0):
        self.gravity = gravity * 50
        self.friction = friction * 50

    def apply_gravity(self, entity: Sprite, dt):
        entity.vsp += self.gravity * dt
        entity.pos.y += entity.vsp * dt
        entity.pos.y = np.clip(entity.pos.y, 100, 500)

    def apply_friction(self, entity: Sprite, dt):
        if entity.hsp > 0:
            entity.hsp -= self.friction * dt
        elif entity.hsp < 0:
            entity.hsp += self.friction * dt
        entity.pos.x += entity.hsp * dt
