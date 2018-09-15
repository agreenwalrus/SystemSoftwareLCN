from sockets.socket_interface import *


class TCPSocket(SocketInterface):

    def __init__(self):
        super().__init__(IPV4_FAMILY_ADDRESS, TCP_SOCKET)

    def send(self, data):
        return self.socket.send(data)

    def recv(self, size_of_data):
        return self.socket.recv(size_of_data)