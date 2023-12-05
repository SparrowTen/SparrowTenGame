from entities.player import Player


class Players:
    def __init__(self):
        self.players = {}

    def add_player(self, id):
        player = Player(0, 0)
        self.players[id] = player
        print(f'[server]: 新增玩家 {id}')

    def update_player(self, id, player_data):
        player = self.players[id]
        player: Player
        player.import_play_data(player_data)
        print(f'[server]: 更新玩家資料 {id}')

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
