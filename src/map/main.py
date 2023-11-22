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
