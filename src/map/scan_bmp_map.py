from pathlib import Path

import numpy as np
import pygame
from PIL import Image

from entities.block import Block
from settings import SETTINGS

from .main import Map

start_num = input('Enter the number of the map you want to scan: ')
end_num = input('Enter the number of the map you want to scan: ')
map_list = []

for i in range(int(start_num), int(end_num) + 1):
    try:
        bmp = Image.open(f'/Users/matt/Desktop/Python/SparrowTenGame/src/assets/map{i}.bmp')
        map_list.append(bmp)
    except FileNotFoundError:
        break

all_maps = []
start_pos = 0

game_map = Map()
for bmp in map_list:
    width, height = bmp.size
    pixels = bmp.load()
    map = []
    for y in range(height):
        map_y = []
        for x in range(width):
            if pixels[x, y] != (0, 0, 0):
                map_y.append(1)
                game_map.add(
                    Block(
                        asset=SETTINGS.WORKDIR + '/assets/block_default.png',
                        start_x=start_pos + x * 64,
                        start_y=y * 64,
                    )
                )
            else:
                map_y.append(0)
        map.append(map_y)
    all_maps.append(map)
    start_pos += 1920
