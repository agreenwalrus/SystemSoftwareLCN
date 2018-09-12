from RequestHandler.request_handler_interface import *
import sys

class FileUploadRequestHandler((RequestHandlerInterface)):

    def parse_params_and_data(self):
        filename, data = self.params_and_data.split(' ', maxsplit=1)
        file_size, data = self.parse_params_and_data.split('\r\n', maxsplit=1)
        return filename, file_size, data

    def handle_request(self, socket):
        try:
            file_name, file_size, data = self.parse_params_and_data()
            file = open('./files/' + file_name, 'wb')
            size = int(file_size)
            size_of_saved_part = 0
            while(len(data) >= 0):
                file.write(data)
                data = socket.recv(2048)
                size_of_saved_part += len(data)
                percent = size_of_saved_part / size
                socket.send(percent)

            file.close()
            return OK
        except IOError:
            return ERROR



