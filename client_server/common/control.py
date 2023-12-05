class Control:
    def __init__(self, player_id):
        self.key_pressed = []

    def read_key_pressed(self):
        return self.key_pressed

    def write_key_pressed(self, key_pressed):
        self.key_pressed = key_pressed
