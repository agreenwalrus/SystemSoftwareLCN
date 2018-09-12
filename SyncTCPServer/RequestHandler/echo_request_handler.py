from RequestHandler.request_handler_interface import RequestHandlerInterface


class EchoRequestHandler(RequestHandlerInterface):

    def handle_request(self, data):
        return data + '\r\n'

    def handle_request(self):
        if len(self.params):
            return ' '.join(self.params) + '\r\n'
        else:
            return ''
