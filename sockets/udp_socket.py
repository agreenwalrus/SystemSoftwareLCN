from sockets.socket_interface import *


class UDPSocket(SocketInterface):

    def __init__(self):
        super().__init__(IPV4_FAMILY_ADDRESS, UDP_SOCKET)

    def send(self, data):
        raise NotImplementedError


    def recv(self, size_of_data):
        raise NotImplementedError