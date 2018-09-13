from RequestHandler.request_handler_interface import *


class EchoRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        if '\r\n' in self.params_and_data:
            params, data = self.parse_params_and_data()
            data_for_sending = (params + '\r\n')
        else:
            data_for_sending = '\r\n'
        socket.send(data_for_sending.encode("cp1252"))
        return OK
