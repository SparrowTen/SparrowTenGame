import pygame
from common.global_variable import GV
from entities.sprite import Sprite
from map.scan_map import game_map, lobby_map


def apply_gravity(entity: Sprite):
    entity.vsp += entity.gravity * GV.TICK
    entity.t_pos.y += entity.vsp * GV.TICK
    return entity


def apply_friction(entity: Sprite):
    if entity.hsp > 0:
        entity.hsp -= entity.friction * GV.TICK
    elif entity.hsp < 0:
        entity.hsp += entity.friction * GV.TICK
    entity.t_pos.x += entity.hsp * GV.TICK
    return entity


def check_ground(player):
    map = None
    if GV.STATE == 'lobby':
        map = lobby_map
    elif GV.STATE == 'game':
        map = game_map

    player.rect.centery = int(
        player.pos.y + player.rect.height / 2 + (player.t_pos.y - player.pos.y)
    )
    if pygame.sprite.spritecollideany(player, map):
        player.rect.centery = int(player.pos.y + player.rect.height / 2)
        player.vsp = 0
        player.jump = True
        player.t_pos.y = player.pos.y
    else:
        player.pos.y = player.t_pos.y

    player.rect.centerx = int(player.pos.x + player.rect.width + (player.t_pos.x - player.pos.x))
    if pygame.sprite.spritecollideany(player, map):
        player.rect.centerx = int(player.pos.x + player.rect.width)
        player.hsp = 0
        player.t_pos.x = player.pos.x
    else:
        player.pos.x = player.t_pos.x
    return player
