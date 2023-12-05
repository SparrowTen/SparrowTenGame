from pathlib import Path

import numpy as np
import pygame
from PIL import Image

from entities.block import Block
from settings import SETTINGS

from .main import Map

img_org = Image.open(f'{SETTINGS.WORKDIR}/assets/map.png').convert('RGB')
arr_org = np.array(img_org)

# ((720, 1280, 3))
res = np.zeros((arr_org.shape[0], arr_org.shape[1], 3), dtype='uint8')

game_map = Map()
for i in range(0, arr_org.shape[0], 64):
    for j in range(0, arr_org.shape[1], 64):
        if np.array_equal(arr_org[i, j], np.array([255, 255, 255])):
            res[i, j] = np.array([153, 229, 80])
        else:
            game_map.add(
                Block(
                    asset=SETTINGS.WORKDIR + '/assets/block_default.png',
                    start_x=j,
                    start_y=i,
                )
            )
