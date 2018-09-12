from RequestHandler.request_handler_interface import RequestHandlerInterface
import sys

class FileUploadRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        file = open('./files/' + self.params[0], 'wb')
        file.write(data)
        file.close()

    def handle_request(self):
        if len(self.params) == 0:
            return "ENTER FILENAME 'upload filename'", self.ERROR
        else:
            return "FILE IS BEING UPLOADED", self.OK




