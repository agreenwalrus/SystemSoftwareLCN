from sockets.buffer.recv_buffer import RecvBuffer
from sockets.buffer.sent_buffer import SentBuffer
from sockets.socket_interface import *
import random
from threading import Thread
import time
from sockets.buffer.buffer import Buffer
import time

#packet structure
#4byte_syn + 4byte_ack + data

BUFFER_DELAY = 0.005 #ms

SENT_BUFFER_SIZE = 10
RECV_BUFFER_SIZE = 10

SYN_START = 0
SYN_END = 7

ACK_START = 8
ACK_END = 15

DATA_START = 16

MIN_PACK_NUM = 0
MAX_PACK_NUM = 3000


class UDPSocket(SocketInterface):

    next_recieve_pack_num = 0
    next_send_pack_num = 0

    connected_socket = ("0.0.0.0", 0)

    def __init__(self):
        super().__init__(IPV4_FAMILY_ADDRESS, UDP_SOCKET)
        self.sent_buffer = SentBuffer(SENT_BUFFER_SIZE)
        self.recv_buffer = RecvBuffer(RECV_BUFFER_SIZE)

    @staticmethod
    def pack_data(syn, ack, data):
        return syn.to_bytes(8, 'big') + ack.to_bytes(8, 'big') + data

    @staticmethod
    def unpack_data(data):
        syn = int.from_bytes(data[SYN_START:SYN_END], byteorder='big', signed=True)
        ack = int.from_bytes(data[ACK_START:ACK_END], byteorder='big', signed=True)
        return syn, ack, data[DATA_START:]

    def listen(self, queue_size):
        pass

    def connect(self, address, port):
        self.connected_socket = (address, port)
        start_pack_num = random.randint(MIN_PACK_NUM, MAX_PACK_NUM)
        self.sent_buffer.set_start_pack_num(start_pack_num)
        self.send('SYN'.encode(ENCODE))
        self.__send_next_pack()
        self.__recv(self.BUF_SIZE)
        self.recv(self.BUF_SIZE)
        self.send('ACK'.encode(ENCODE))
        self.__send_next_pack()
        Thread(target=self.__send_next_pack).start()
        Thread(target=self.__recv, args=(self.BUF_SIZE, )).start()

    def accept(self):
        self.__recv(self.BUF_SIZE)
        self.recv(self.BUF_SIZE)
        self.send('SYN ACK'.encode(ENCODE))
        self.__send_next_pack()
        self.__recv(self.BUF_SIZE)
        self.recv(self.BUF_SIZE)
        Thread(target=self.__send_next_pack).start()
        Thread(target=self.__recv, args=(self.BUF_SIZE,)).start()
        return self, self.connected_socket

    def __send_next_pack(self):
        if self.sent_buffer.get_current_size() > 0:
            syn, data = self.sent_buffer.get_next_pack()
        packed_data = UDPSocket.pack_data(syn, self.recv_buffer.get_ack(), data)
        return self.socket.sendto(packed_data, self.connected_socket)

    def __recv(self, size_of_data):
        data, self.connected_socket = self.socket.recvfrom(size_of_data)
        syn, ack, data = UDPSocket.unpack_data(data)
        print("recieved ", syn, ack, data)
        if self.recv_buffer.is_possible_to_add_pack(syn):
            self.sent_buffer.delete_pack(ack)
            self.recv_buffer.add_pack(syn, data)
        return

    def send(self, data):
        if self.sent_buffer.get_current_size() < self.sent_buffer.get_buffer_capacity():
            self.sent_buffer.add_pack(data)
        return

    def recv(self, size_of_data):
        while self.recv_buffer.get_current_size() == 0:
            time.sleep(0.005)
        return self.recv_buffer.pop_next_pack()


    # @staticmethod
    # def pack_data(syn, ack, data):
    #     return syn.to_bytes(8, 'big') + ack.to_bytes(8, 'big') + data
    #
    # @staticmethod
    # def unpack_data(data):
    #     syn = int.from_bytes(data[SYN_START:SYN_END], byteorder='big', signed=False)
    #     ack = int.from_bytes(data[ACK_START:ACK_END], byteorder='big', signed=False)
    #     return syn, ack, data[DATA_START:]
    #
    # def listen(self, queue_size):
    #     pass
    #
    # def connect(self, address, port):
    #     self.connected_socket = (address, port)
    #     self.next_send_pack_num = random.randint(MIN_PACK_NUM, MAX_PACK_NUM)
    #     self.send('SYN'.encode(ENCODE))
    #     self.recv(self.BUF_SIZE)
    #     self.send('ACK'.encode(ENCODE))
    #
    # def accept(self):
    #     self.recv(self.BUF_SIZE)
    #     self.send('SYN ACK'.encode(ENCODE))
    #     self.recv(self.BUF_SIZE)
    #     return self, self.connected_socket
    #
    # def __send(self, syn, ack, data):
    #     packed_data = UDPSocket.pack_data(syn, ack, data)
    #     return self.socket.sendto(packed_data, self.connected_socket)
    #
    # def __recv(self, size_of_data):
    #     data, self.connected_socket = self.socket.recvfrom(size_of_data)
    #     print("connected ", self.connected_socket)
    #     return UDPSocket.unpack_data(data)
    #
    # def send(self, data):
    #     self.next_send_pack_num += 1
    #     while self.sent_buffer.size >= self.sent_buffer.max_size:
    #         time.sleep(BUFFER_DELAY)
    #     self.sent_buffer.add(self.next_send_pack_num, data)
    #     return
    #
    # def recv(self, size_of_data):
    #     while self.sent_buffer.size == 0:
    #         time.sleep(BUFFER_DELAY)
    #     syn, ack, data = self.__recv(size_of_data)
    #     return data
    # *//
