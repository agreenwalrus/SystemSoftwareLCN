import socket
import sys
import os
import progressbar
from client.client_interface import ClientInterface
import request_handler.client_request_handler.client_request_handler_interface as rh


class SerialTCPSocketClient(ClientInterface):
    def __init__(self,  ipv4_addr, port, request_handler_factory):
        super().__init__(ipv4_addr, port, request_handler_factory)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        self.socket.connect((self.ipv4_addr, self.port))
        print("Connection with ", self.ipv4_addr, ":", self.port, " is established.")
        code = rh.OK
        while code != rh.STOP_CLIENT:
            input_line = input()
            request_handler = self.request_handler_factory.get_request_handler(input_line)
            code, message = request_handler.handle_request(self.socket)
            print(message)
            print("Code of operation: ", code)

        self.stop_client()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_client(self):
        self.__shutdown()