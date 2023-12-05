from pathlib import Path

import numpy as np
import pygame
from PIL import Image

from entities.block import Block
from settings import SETTINGS


class Map(pygame.sprite.Group):
    def render(self, screen, pos_offset: pygame.Vector2() = pygame.Vector2(0, 0)):
        for block in self.sprites():
            block: Block
            block.render(screen, pos_offset)


# game_map = Map()

# print(res.shape)
# res = Image.fromarray(res, "RGB")
# res.show()
# for i in range(0, SETTINGS.SCREEN[0], 64):
#     game_map.add(
#         Block(
#             asset=SETTINGS.WORKDIR + '/assets/block_default.png',
#             start_x=i,
#             start_y=SETTINGS.SCREEN[1] - 64,
#         )
#     )
# game_map.add(
#     Block(
#         asset=SETTINGS.WORKDIR + '/assets/block_default.png',
#         start_x=256,
#         start_y=SETTINGS.SCREEN[1] - 128,
#     )
# )
# for i in range(128, 256, 64):
#     game_map.add(
#         Block(
#             asset=SETTINGS.WORKDIR + '/assets/block_default.png',
#             start_x=384,
#             start_y=SETTINGS.SCREEN[1] - i,
#         )
#     )