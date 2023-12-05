import socket
import threading
import time

from entities.player import player
from settings import SETTINGS

from .utils import packet_deserializer, packet_serializer


class ClientSocket:
    def __init__(self):
        self.buffer_size = SETTINGS.BUFFER_SIZE
        self.server_addr = (SETTINGS.SERVER_IP, SETTINGS.SERVER_PORT)
        self.t_update_players = threading.Thread(target=self.update_player_on_server)

    def create_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client.connect(self.server_addr)
        self.client.setblocking(False)

    def send_to_server(self, data):
        packet = packet_serializer(data)
        self.client.send(packet)

    def get_new_data(self):
        data = None
        try:
            data = self.client.recv(self.buffer_size)
            return packet_deserializer(data)
        except Exception as e:
            return data

    def update_player_on_server(self):
        while True:
            player_data = player.export_player_data()
            self.send_to_server(player_data)
            time.sleep(1)

    def close(self):
        self.client.close()
