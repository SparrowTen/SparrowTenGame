import threading


class Players:
    def __init__(self):
        self.players = {}
        self.player_data_dict = {
            'id': 0,
            'jump': False,
            'pos': (0, 0),
            't_pos': (0, 0),
            'vsp': 0,
            'hsp': 0,
            'gravity': 0,
            'friction': 0,
            'self.gravity': 0,
            'self.friction': 0,
        }
        self.lock = threading.Lock()

    def read_players(self, id):
        # 確定沒有人在寫入
        with self.lock:
            return self.players[id]

    def write_players(self, **player_data):
        with self.lock:
            self.lock.acquire()
            self.players[player_data['id']] = player_data
            self.lock.release()


players = Players()
