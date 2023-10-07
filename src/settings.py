import os


class Settings:
    def __init__(self):
        self.SCREEN = (1280, 720)
        self.WORKDIR = os.path.dirname(os.path.abspath(__file__))


SETTINGS = Settings()
