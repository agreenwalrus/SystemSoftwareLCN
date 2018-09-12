from RequestHandler.request_handler_interface import *


class FileDownloadRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        try:
            file_name, data = self.parse_params_and_data()
            file = open('./files/' + file_name, 'r')
            #ХЗ
            size = 10240
            ######################################
            size_of_read_part = 0
            data = file.read(size_of_read_part)
            while size - size_of_read_part != 0:
                socket.send(data)
                size_of_read_part += len(data)
                percent = size_of_read_part / size
                data = file.read(size_of_read_part)

            file.close()
            return OK
        except IOError:
            return ERROR

