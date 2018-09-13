from RequestHandler.request_handler_interface import *
import datetime

class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, socket):
        socket.sendall((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\r\n').encode("cp1252"))
        return OK

