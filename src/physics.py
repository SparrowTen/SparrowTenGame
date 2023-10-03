import numpy as np
from entities.move_object import MoveObject

class Physics:
    def __init__(self, gravity = 9.8, friction = 5.0):
        self.gravity = gravity * 50
        self.friction = friction * 50
    
    def apply_gravity(self, entity : MoveObject, dt):
        entity.velocity_y += self.gravity * dt
        entity.pos.y += entity.velocity_y * dt
        entity.pos.y = np.clip(entity.pos.y, 100, 500)
    
    def apply_friction(self, entity : MoveObject, dt):
        if entity.velocity_x > 0:
            entity.velocity_x -= self.friction * dt
        elif entity.velocity_x < 0:
            entity.velocity_x += self.friction * dt
        entity.pos.x += entity.velocity_x * dt