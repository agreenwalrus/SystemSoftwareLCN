class ServerInterface:

    def __init__(self, ipv4_addr, port, request_handler_factory):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.request_handler_factory = request_handler_factory

    def start_server(self):
        raise NotImplementedError

    def stop_server(self):
        raise NotImplementedError


