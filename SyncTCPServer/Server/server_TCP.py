from Server.server_interface import ServerInterface
import socket


class SerialTCPSocketServer(ServerInterface):

    
    QUEUE_FOR_CONNECTORS_SIZE = 1

    def __init__(self, ipv4_addr, port, request_handler_factory):
        super.__init__(ipv4_addr, port, request_handler_factory)
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
    def start_server(self):
        self.socket.bind(self.ipv4_addr, self.port)
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)

        while 1:
            client_socket, client_addr = self.socket.accept()
            #нет гарантий, что команда поместиться в эту строку. Надо уточнить
            recieved_data = client_socket.recv(2048)
            command_and_params, data = recieved_data.split('\n', maxsplit=1)
            request_handler = self.request_handler_factory.get_request_handler(command_and_params)

            while len(data):
                client_socket.send(request_handler.handle_request(data))
                data = client_socket.recv(2048)


    def stop_server(self):
        pass

