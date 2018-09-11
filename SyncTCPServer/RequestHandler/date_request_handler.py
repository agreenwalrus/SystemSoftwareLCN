from RequestHandler.request_handler_interface import RequestHandlerInterface


class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        raise NotImplementedError
