from RequestHandler.request_handler_interface import *


class ExitRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        return STOP_SERVER
