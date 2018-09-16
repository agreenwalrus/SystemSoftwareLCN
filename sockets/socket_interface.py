from socket import socket

IPV4_FAMILY_ADDRESS = socket.AF_INET
TCP_SOCKET = socket.SOCK_STREAM
UDP_SOCKET = socket.SOCK_DGRAM


class SocketInterface:

    def __init__(self, address_family, socket_type):
        self.socket = socket(address_family, socket_type)


    def connect(self, address, port):
        return self.socket.connect((address, port))

    def bind(self, address, port):
        return self.socket.bind((address, port))

    def listen(self, queue_size):
        return self.socket.listen(queue_size)

    def  accept(self):
        return self.socket.accept()

    def shutdown(self, how):
        return self.socket.shutdown(how)

    def close(self, ):
        return self.socket.close()

    def send(self, data):
        raise NotImplementedError

    def recv(self, size_of_data):
        raise NotImplementedError

