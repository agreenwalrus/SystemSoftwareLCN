class RequestHandlerInterface:

    def __init__(self, params):
        self.params = params

    def handle_request(self):
        raise NotImplementedError

    def handle_request(self, data):
        raise NotImplementedError
