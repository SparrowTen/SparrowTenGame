from pygame import Rect

from entities.sprite import Sprite


class Block(Sprite):
    def __init__(self, asset, start_x, start_y):
        super().__init__(asset, start_x, start_y)
        self.rect = Rect(
            start_x,
            start_y,
            self.asset.get_width(),
            self.asset.get_height(),
        )

        self.rect.center = (
            int(start_x + self.asset.get_width() / 2),
            int(start_y + self.asset.get_height() / 2),
        )
