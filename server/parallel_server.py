from sockets.socket_interface import ENCODE
from request_handler.server_request_handler import server_request_handler_interface
from threading import Lock


class ParallelServer:
    RUN_SERVER = 1
    STOP_SERVER = 0
    CLIENT_TIMEOUT = 10

    __running_server = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 10

    def process_client(self, client_socket):
        try:
            code = server_request_handler_interface.OK
            while code != server_request_handler_interface.STOP_SERVER:
                recieved_data = ''
                while '\n' not in recieved_data:
                    recieved_data += client_socket.recv(2048).decode("cp1252")

                print(recieved_data)
                request_handler = self.request_handler_factory.get_request_handler(recieved_data)
                code = request_handler.handle_request(client_socket)
                print("Code of operation: ", code)
        except ConnectionAbortedError:
            print("Client ", client_socket, " has disconnected")
        finally:
            client_socket.close()
            self.__change_current_amount_of_clients__(-1)

    def __init__(self, ipv4_addr, port, socket, request_handler_factory, max_amount_of_clients, pool):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.socket = socket
        self.request_handler_factory = request_handler_factory
        self.max_amount_of_clients = max_amount_of_clients
        self.current_amount_of_clients = 0
        self.pool = pool(max_amount_of_clients)
        self.lock = Lock()
        # self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def __change_current_amount_of_clients__(self, delta):
        self.lock.acquire()
        self.current_amount_of_clients += delta
        self.lock.release()

    def start_server(self):
        self.socket.bind((self.ipv4_addr, self.port))
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server = self.RUN_SERVER

        while self.__running_server == self.RUN_SERVER:
            client_socket, client_addr = self.socket.accept()
            print("Here is a client ", client_addr)
            if self.current_amount_of_clients < self.max_amount_of_clients:
                client_socket.send("Welcome!".encode(ENCODE))
                print("Connection is established with ", client_addr)
                self.pool.execute(self.process_client, client_socket)
                self.__change_current_amount_of_clients__(1)
            else:
                client_socket.close()
        self.pool.shutdown(self.CLIENT_TIMEOUT)
        self.__shutdown()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_server(self):
        self.__running_server = self.STOP_SERVER


