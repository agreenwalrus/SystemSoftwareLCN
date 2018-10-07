from server.multiplex_server import MultiplexerServer
from request_handler_factory.rhf_server.multiplex_remote_console_request_handler_factory import MultiplexRemoteConsoleRequestHandlerFactory
from sockets.tcp_socket import *
#from sockets.tcp_socket import TCPSocket

server = MultiplexerServer("0.0.0.0", 37000, socket(AF_INET, SOCK_STREAM), MultiplexRemoteConsoleRequestHandlerFactory())
server.start_server()

# if __name__=='__main__':
#     address = ''
#     while not re.match(
#             '^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$',
#             address):
#         print('ipv4 : ', end='')
#         address = input()
#
#     port = -1
#     while port < 0 or port > 65235:
#         print('port : ', end='')
#         try:
#             port = int(input())
#         except ValueError:
#             continue
#     try:
#         server = SerialTCPSocketServer(address, port, UDPSocket(), RemoteConsoleRequestHandlerFactory())
#         server.start_server()
#     except ConnectionRefusedError:
#         print('Connection is refused')
