import select
import socket

from common.players import players
from settings import SETTINGS

from .utils import packet_deserializer, packet_serializer


class ServerSocket:
    def __init__(self):
        self.buffer_size = SETTINGS.BUFFER_SIZE
        self.ports = [SETTINGS.SERVER_PORT]
        self.inputs = []
        self.outputs = []
        self.srv_list = []

    def create_socket(self):
        for port in self.ports:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((SETTINGS.SERVER_IP, port))
            server.setblocking(False)
            server.listen(self.buffer_size)
            self.inputs.append(server)
            self.srv_list.append(server)
            print('[server]: 監聽在 ' + str(port))

    def send_to_client(self, client, data):
        packet = packet_serializer(data)
        client.send(packet)

    def listen(self):
        readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
        s: socket.socket
        for s in readable:
            if s in self.srv_list:
                connection, (rip, rport) = s.accept()
                connection.setblocking(False)
                self.inputs.append(connection)
                players.add_player(rport)
                print('[server]: ' + str(rport) + ' 已連線')
            else:
                try:
                    raw_data = s.recv(self.buffer_size)
                    if raw_data:
                        player_id = s.getpeername()[1]  # 玩家的 port 當作 id
                        player_data = dict(packet_deserializer(raw_data))
                        if player_data['id'] == 0:
                            player_data['id'] = player_id
                        players.server_update_player(player_id, player_data)
                        players.calculate_player_data()
                        players_data = players.pack_player_data()
                        print(players_data)
                        self.send_to_client(s, players_data)
                except Exception as e:
                    print(e)
