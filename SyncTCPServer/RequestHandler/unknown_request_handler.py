from RequestHandler.request_handler_interface import RequestHandlerInterface


class UnknownRequestHandler(RequestHandlerInterface):

    def handle_request(self, data):
        return "Unknown command!\n"

