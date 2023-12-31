import socket
import threading

from common.players import players
from entities.player import player
from settings import SETTINGS

from .utils import packet_deserializer, packet_serializer


class ClientSocket:
    def __init__(self):
        self.buffer_size = SETTINGS.BUFFER_SIZE
        self.server_addr = (SETTINGS.SERVER_IP, SETTINGS.SERVER_PORT)
        self.t_update_player_and_get_data = threading.Thread(target=self.update_player_and_get_data)

    def create_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client.connect(self.server_addr)
        self.client.settimeout(1)

    def send_to_server(self, data):
        packet = packet_serializer(data)
        self.client.send(packet)

    def get_new_data(self):
        data = None
        try:
            data = self.client.recv(self.buffer_size)
            return packet_deserializer(data)
        except Exception as e:
            print(e)
            return data

    def update_player_and_get_data(self):
        while True:
            player_data = player.export_player_data()
            player_data['key_pressed'] = player.get_key_pressed()
            self.send_to_server(player_data)
            new_data = self.get_new_data()
            if new_data:
                new_data: dict
                player.import_player_data(new_data.get(player.id))
                new_data.pop(player.id)
                players.client_import_other_players_data(new_data)

    def close(self):
        self.client.close()
