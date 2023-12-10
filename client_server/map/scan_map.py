import numpy as np
import pygame
from entities.block import Block
from PIL import Image
from settings import SETTINGS


class Map(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        img_org = Image.open(f'{SETTINGS.WORKDIR}/assets/map.png').convert('RGB')
        self.arr_org = np.array(img_org)

        # ((720, 1280, 3))
        self.res = np.zeros((self.arr_org.shape[0], self.arr_org.shape[1], 3), dtype='uint8')

    def generate_game_map(self):
        for i in range(0, self.arr_org.shape[0], 64):
            for j in range(0, self.arr_org.shape[1], 64):
                if np.array_equal(self.arr_org[i, j], np.array([255, 255, 255])):
                    self.res[i, j] = np.array([153, 229, 80])
                else:
                    self.add(
                        Block(
                            asset=SETTINGS.WORKDIR + '/assets/block_default.png',
                            start_x=j,
                            start_y=i,
                        )
                    )

    def generate_lobby_map(self):
        for i in range(0, SETTINGS.SCREEN[0], 64):
            self.add(
                Block(
                    asset=SETTINGS.WORKDIR + '/assets/block_default.png',
                    start_x=i,
                    start_y=SETTINGS.SCREEN[1] - 64,
                )
            )

    def change_map(self, map_type):
        self.empty()
        if map_type == 'lobby':
            self.generate_game_map()
            # self.generate_lobby_map()
        elif map_type == 'game':
            self.generate_game_map()

    def render(self, screen, pos_offset: pygame.Vector2() = pygame.Vector2(0, 0)):
        for block in self.sprites():
            block: Block
            block.render(screen, pos_offset)


map = Map()
map.change_map('lobby')
