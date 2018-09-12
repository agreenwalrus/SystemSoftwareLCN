from Server.server_interface import ServerInterface
from RequestHandler import request_handler_interface
import socket


class SerialTCPSocketServer(ServerInterface):

    RUN_SERVER = 1
    STOP_SERVER = 0

    __running_server = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 1

    def __init__(self, ipv4_addr, port, request_handler_factory):
        super().__init__(ipv4_addr, port, request_handler_factory)
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
    def start_server(self):
        self.socket.bind((self.ipv4_addr, self.port))
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server = self.RUN_SERVER

        client_socket, client_addr = self.socket.accept()
        client_socket.recv(2048)
        self.socket.setblocking(0)
        while self.__running_server == self.RUN_SERVER:
            recieved_data = ''
            while '\n' not in recieved_data:
                recieved_data += client_socket.recv(2048).decode("cp1252")
            print(recieved_data)
            request_handler = self.request_handler_factory.get_request_handler(recieved_data)
            code = request_handler.handle_request(client_socket)
            if code == request_handler_interface.STOP_SERVER or code == request_handler_interface.STOP_SERVER:
                break

        self.stop_server()

    def __shutdown(self):
        self.socket.shutdown()
        self.socket.close()

    def stop_server(self):
        self.__running_server = self.STOP_SERVER

