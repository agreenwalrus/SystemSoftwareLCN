from RequestHandler.request_handler_interface import RequestHandlerInterface
import datetime

class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\r\n'

    def handle_request(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\r\n'

