OK = 0
ERROR = 1
STOP_SERVER = 2
ENCODE = "cp1252"

# code:
#     0 - OK
#     1 - ERROR
#     2 - StopServer


class RequestHandlerWrapper:

    def __init__(self, request_handler_factory):
        self.commad = ''
        self.initialized = False
        self.request_handler = None
        self.request_handler_factory = request_handler_factory

    def handle_request(self, data):
        if self.initialized:
            is_alive, code, message = self.request_handler.handle_request(data)
            if not is_alive:
                self.initialized = False
        else:
            self.commad += data
            if '\n' in data:
                self.request_handler = self.request_handler_factory.get_request_handler(data)
                self.initialized = True
