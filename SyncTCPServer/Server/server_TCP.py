import socketserver
from Server.server_interface import ServerInterface


class TCPServer(ServerInterface):

    def __init__(self,interface = '', ipv4_addr, port, request_handler):
        self.interface = interface
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.request_handler = request_handler

        # self.socket = socket.socket()
        # self.socket.bind(self.interface, port) #'' - all interface
        # self.socket.connect((self.ipv4_addr, self.port))
        
    def start_server(self):
        with socketserver.TCPServer((self.ipv4_addr, self.port), self.request_handler) as server:
            self.server = server
            self.server.serve_forever()
        

    def stop_server(self):
        self.server.shutdown()
