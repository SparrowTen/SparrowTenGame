import pygame

from entities.sprite import Sprite

# from map.main import game_map
from map.scan_bmp_map import game_map


class Physics:
    def __init__(self, gravity=9.8, friction=5.0):
        self.gravity = gravity * 50
        self.friction = friction * 50

    def apply_gravity(self, entity: Sprite, dt):
        entity.vsp += self.gravity * dt
        entity.t_pos.y += entity.vsp * dt

    def apply_friction(self, entity: Sprite, dt):
        if entity.hsp > 0:
            entity.hsp -= self.friction * dt
        elif entity.hsp < 0:
            entity.hsp += self.friction * dt
        entity.t_pos.x += entity.hsp * dt

    def check_ground(self, entity: Sprite):
        entity.rect.centery = int(
            entity.pos.y + entity.rect.height / 2 + (entity.t_pos.y - entity.pos.y)
        )
        if pygame.sprite.spritecollideany(entity, game_map):
            entity.rect.centery = int(entity.pos.y + entity.rect.height / 2)
            entity.vsp = 0
            entity.jump = True
            entity.t_pos.y = entity.pos.y
        else:
            entity.pos.y = entity.t_pos.y

        entity.rect.centerx = int(
            entity.pos.x + entity.rect.width + (entity.t_pos.x - entity.pos.x)
        )
        if pygame.sprite.spritecollideany(entity, game_map):
            entity.rect.centerx = int(entity.pos.x + entity.rect.width)
            entity.hsp = 0
            entity.t_pos.x = entity.pos.x
        else:
            entity.pos.x = entity.t_pos.x
