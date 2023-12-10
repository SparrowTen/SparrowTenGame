from entities.player import Player


class Players:
    def __init__(self):
        self.players = {}

    def add_player(self, id):
        player = Player(0, 0)
        self.players[id] = player

    def server_update_player(self, id, player_data):
        player = self.players[id]
        player: Player
        player.import_player_data(player_data)
        player.set_key_pressed(player_data['key_pressed'])

    def client_import_other_players_data(self, players_data):
        for id in players_data:
            player_data = players_data[id]
            if id not in self.players:
                self.add_player(id)
            player = self.players[id]
            player: Player
            player.import_player_data(player_data)
            player.update_player_skin(player_data['skin_id'])

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
