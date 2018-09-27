from socket import *

IPV4_FAMILY_ADDRESS = AF_INET
TCP_SOCKET = SOCK_STREAM
UDP_SOCKET = SOCK_DGRAM

ENCODE = "cp1252"
PACKAGE_SIZE = 10240
USEFUL_PACKAGE_SIZE = PACKAGE_SIZE - 8

class SocketInterface:

    BUF_SIZE = 2048

    def __init__(self, address_family, socket_type):
        self.socket = socket(address_family, socket_type)

    def bind(self, address, port):
        return self.socket.bind((address, port))

    def shutdown(self, how):
        return self.socket.shutdown(how)

    def close(self):
        return self.socket.close()

    def send(self, data):
        raise NotImplementedError

    def recv(self, size_of_data):
        raise NotImplementedError

