import pygame

from entities.block import Block
from settings import SETTINGS


class Map(pygame.sprite.Group):
    def render(self, screen):
        for block in self.sprites():
            block: Block
            block.render(screen)


game_map = Map()
for i in range(0, SETTINGS.SCREEN[0], 64):
    game_map.add(
        Block(
            asset=SETTINGS.WORKDIR + '/assets/block_default.png',
            start_x=i,
            start_y=SETTINGS.SCREEN[1] - 64,
        )
    )
game_map.add(
    Block(
        asset=SETTINGS.WORKDIR + '/assets/block_default.png',
        start_x=256,
        start_y=SETTINGS.SCREEN[1] - 128,
    )
)
