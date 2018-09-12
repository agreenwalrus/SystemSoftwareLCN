OK = 1
ERROR = 0
STOP_SERVER = 2


class RequestHandlerInterface:

    def __init__(self, data):
        self.params_and_data = data

    def parse_params_and_data(self):
        params, data = self.params_and_data.split('\r\n', maxsplit=1)
        return params, data

    def handle_request(self, socket):
        raise NotImplementedError
