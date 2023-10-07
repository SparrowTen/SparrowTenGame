import os


class Settings:
    def __init__(self):
        self.SCREEN = (1280, 720)  # (640, 360), (320, 180), (160, 90), (80, 45)
        self.WORKDIR = os.path.dirname(os.path.abspath(__file__))


SETTINGS = Settings()
