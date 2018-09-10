class ServerInterface:

    def __init__(self, ipv4_addr, port, request_handler):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.request_handler = request_handler

    def start_server(self):
        raise NotImplementedError

    def stop_server(self):
        raise NotImplementedError


