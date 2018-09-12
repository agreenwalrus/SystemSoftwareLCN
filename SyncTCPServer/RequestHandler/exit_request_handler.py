from RequestHandler.request_handler_interface import RequestHandlerInterface


class ExitRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        raise NotImplementedError
