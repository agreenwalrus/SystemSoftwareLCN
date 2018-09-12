from RequestHandler.request_handler_interface import *


class UnknownRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.send("Unknown command!\r\n".encode("cp1252"))
        return OK

