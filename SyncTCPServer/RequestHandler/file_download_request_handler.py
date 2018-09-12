from RequestHandler.request_handler_interface import RequestHandlerInterface


class FileDownloadRequestHandler(RequestHandlerInterface):

    def handle_request(self, data):
        file = open('./files/' + self.params[0], 'wb')
        file.read(data)
        file.close()

    def handle_request(self):
        return "FILE IS BEING UPLOADED", self.OK
