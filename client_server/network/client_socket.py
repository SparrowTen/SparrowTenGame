import socket

import pygame
from common.players import Players

from ..settings import SETTINGS
from .utils import packet_deserializer, packet_serializer


class ClientSocket:
    def __init__(self):
        self.buffer_size = SETTINGS.BUFFER_SIZE
        self.server_addr = (SETTINGS.SERVER_IP, SETTINGS.SERVER_PORT)

    def create_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client.connect(self.server_addr)
        self.client.setblocking(False)

    def collect_key_pressed(self):
        data = {'key_pressed': []}
        keys = pygame.key.get_pressed()
        for key, value in enumerate(keys):
            if value:
                data['key_pressed'].append(key)
        return data

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

    def bk_update_players(self):
        while True:
            key_pressed = self.collect_key_pressed()
            if key_pressed:
                self.send_to_server(key_pressed)
            data_from_server = self.get_new_data()
            if data_from_server:
                print(data_from_server)

    def close(self):
        self.client.close()
