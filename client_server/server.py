from network.server_socket import ServerSocket

if __name__ == '__main__':
    server = ServerSocket()
    server.create_socket()
    server.listen()
