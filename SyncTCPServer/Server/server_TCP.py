from Server.server_interface import ServerInterface
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
            command_and_params, data = recieved_data.split('\r\n', maxsplit=1)
            if command_and_params == 'exit':
                self.stop_server()
            else:
                request_handler = self.request_handler_factory.get_request_handler(command_and_params)
                client_socket.send(request_handler.handle_request().encode("cp1252"))

                while len(data):
                    client_socket.send(request_handler.handle_request(data).encode("cp1252"))
                    data = client_socket.recv(2048)

        self.stop_server()

    def __shutdown(self):
        self.socket.shutdown()
        self.socket.close()

    def stop_server(self):
        self.__running_server = self.STOP_SERVER

