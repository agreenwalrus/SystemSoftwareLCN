from RequestHandler.request_handler_interface import RequestHandlerInterface


class FileDownloadRequestHandler(RequestHandlerInterface):

    def handle_request(self, data):
        raise NotImplementedError
