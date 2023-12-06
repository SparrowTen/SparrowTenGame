import os


class Settings:
    def __init__(self):
        self.SCREEN = (720, 360)  # (640, 360), (320, 180), (160, 90), (80, 45)
        self.WORKDIR = os.path.dirname(os.path.abspath(__file__))
        self.DEBUG = True

        self.SERVER_IP = '127.0.0.1'
        self.SERVER_PORT = 9239
        self.CLIENT_ID = 1
        self.BUFFER_SIZE = 4096


SETTINGS = Settings()
