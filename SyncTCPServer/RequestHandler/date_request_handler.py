from SyncTCPServer.RequestHandler.request_handler_interface import RequestHandlerInterface
import datetime

class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        return str(datetime.datetime.now())
