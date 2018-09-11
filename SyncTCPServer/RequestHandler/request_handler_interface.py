class RequestHandlerInterface:

    def __init__(self, params):
        self.__params = params

    def handle_request(self, data):
        raise NotImplementedError
