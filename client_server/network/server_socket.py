import select
import socket

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

    def listen(self):
        while True:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
            s: socket.socket
            for s in readable:
                if s in self.srv_list:
                    connection, (rip, rport) = s.accept()
                    connection.setblocking(False)
                    self.inputs.append(connection)
                    laddr = connection.getsockname()
                    print(f'[server]: 接受來自 ({str(rip)}, {rport}) 的連線')
                else:
                    try:
                        raw_data = s.recv(self.buffer_size)
                        if raw_data:
                            raddr = s.getpeername()
                            laddr = s.getsockname()
                            uppack_data = packet_deserializer(raw_data)
                            print(
                                f'[server]: 在 {str(laddr)} 收到來自 ({str(raddr[0])}, {raddr[1]}) 的資料 \n {uppack_data}'
                            )
                    except Exception as e:
                        print(e)
