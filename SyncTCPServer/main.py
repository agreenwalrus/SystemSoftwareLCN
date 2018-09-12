from SyncTCPServer.Server.server_TCP import SerialTCPSocketServer
from SyncTCPServer.remote_console_request_handler_factory import RemoteConsoleRequestHandlerFactory

if __name__ == '__main__':
    server = SerialTCPSocketServer('127.0.0.1',39004, RemoteConsoleRequestHandlerFactory());
    server.start_server()
