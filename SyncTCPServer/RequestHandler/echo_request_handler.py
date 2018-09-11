from RequestHandler.request_handler_interface import RequestHandlerInterface


class EchoRequestHandler(RequestHandlerInterface):

    def handle_request(self, data):
        return data
