from sockets.socket_interface import ENCODE
import socket
import select
from request_handler.multiplex_server_request_handler.request_handler_wrapper import *
from server.server_interface import ServerInterface
import queue


class MultiplexerServer(ServerInterface):
    RUN_SERVER = 1
    STOP_SERVER = 0
    TIMEOUT = 120
    BUFFER_SIZE = 1024

    __running_server__ = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 1

    def __init__(self, ipv4_addr, port, socket, request_handler_factory):
        super().__init__(ipv4_addr, port, socket, request_handler_factory)
        # self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.request_handler_wrappers = {}
        self.write_data = {}
        self.read_list_sockets = []
        self.write_list_sockets = []

    def process_write_list(self, sockets):
        for s in sockets:
            self.request_handler_wrappers[s]
            try:
                next_msg = self.write_data[s].get_nowait()
            except queue.Queue.Empty:
                # No messages waiting so stop checking for writability.
                self.write_list_sockets.remove(s)
            else:
                s.send(next_msg)

    def process_read_list(self, sockets):
        for s in sockets:
            if s is self.socket:
                client_socket, client_addr = self.socket.accept()
                print("Connection is established with ", client_addr)
                self.read_list_sockets.append(client_socket)
                self.request_handler_wrappers[s] = RequestHandlerWrapper(self.request_handler_factory)
                self.write_data[s] = queue.Queue(self.QUEUE_FOR_CONNECTORS_SIZE)
            else:
                recv_data = s.recv(self.BUFFER_SIZE)
                code, data = self.request_handler_wrappers[s].handle_request(recv_data)
                if code == STOP_SERVER:
                    self.process_disconnect(s)
                elif code == OK and data is not '':
                    self.write_data[s].put(data)
                    if socket not in self.write_list_sockets:
                        self.write_list_sockets.append(s)
                else:
                    if socket in self.write_list_sockets:
                        self.write_list_sockets.remove(s)

    def process_disconnect(self, socket):
        self.read_list_sockets.remove(socket)
        self.request_handler_wrappers.remove(socket)
        self.write_data.remove(socket)
        if socket in self.write_list_sockets:
            self.write_list_sockets.remove(s)
        socket.close()

    def process_except_list(self, sockets):
        for s in sockets:
            self.process_disconnect(s)

    def start_server(self):

        self.socket.bind((self.ipv4_addr, self.port))
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server__ = self.RUN_SERVER

        self.read_list_sockets.append(self.socket)

        while self.__running_server__ == self.RUN_SERVER:
            print("Select start")

            read, write, excpt = select.select(self.read_list_sockets,
                                               self.write_list_sockets,
                                               self.read_list_sockets)
            print("read ", read)
            if (len(read) == 0
                    and len(write) == 0
                    and len(excpt) == 0):
                self.stop_server()

            self.process_read_list(read)
            self.process_write_list(write)
            self.process_except_list(excpt)
        self.__shutdown()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_server(self):
        self.__running_server__ = self.STOP_SERVER


