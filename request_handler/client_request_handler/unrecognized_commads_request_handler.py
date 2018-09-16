from request_handler.client_request_handler.client_request_handler_interface import *


class UnrecognizedCommandsRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.sendall((self.request + "\r\n").encode(ENCODE))
        return OK, socket.recv(1024).decode(ENCODE)

