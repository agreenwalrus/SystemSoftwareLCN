class ClientInterface:

    def __init__(self, ipv4_addr, port, request_handler_factory):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.request_handler_factory = request_handler_factory

    def __shutdown(self):
        raise NotImplementedError

    def start_client(self):
        raise NotImplementedError

    def stop_client(self):
        raise NotImplementedError


