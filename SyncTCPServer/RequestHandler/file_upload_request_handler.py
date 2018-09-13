from RequestHandler.request_handler_interface import *
import sys

class FileUploadRequestHandler((RequestHandlerInterface)):

    def parse_params_and_data(self):
        filename, data = self.params_and_data.split(' ', maxsplit=1)
        file_size, data = data.split('\r\n', maxsplit=1)
        return filename, file_size, data

    def handle_request(self, socket):
        try:
            file_name, file_size, data = self.parse_params_and_data()
            file = open('./files/' + file_name, 'w+b')
            file_size_remaining = int(file_size)

            socket.send(bytes('123', 'cp1252')) #sync
            while file_size_remaining != 0:

                data = socket.recv(1024)
                file.write(data)
                file_size_remaining -= len(data)
                print(file_size_remaining)

            file.close()
            return OK
        except IOError:
            return ERROR



