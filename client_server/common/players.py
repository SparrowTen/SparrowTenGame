from entities.player import Player


class Players:
    def __init__(self):
        self.players = {}

    def add_player(self, id):
        player = Player(0, 0)
        self.players[id] = player

    def update_player(self, id, player_data):
        player = self.players[id]
        player: Player
        player.import_player_data(player_data)

    def calculate_player_data(self):
        for id in self.players:
            player = self.players[id]
            player: Player
            player.update()

    def pack_player_data(self):
        players_data = {}
        for id in self.players:
            player = self.players[id]
            player: Player
            players_data[player.id] = player.export_player_data()
        return players_data


players = Players()
