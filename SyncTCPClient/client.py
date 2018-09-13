import socket
import sys
import os
import progressbar


class  SerialTCPSocketClient:
    def __init__(self,  ipv4_addr, port):
        self.ipv4_addr = ipv4_addr
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        self.socket.connect((self.ipv4_addr, self.port))
        input_line = ''
        while input_line != 'exit':
            input_line = input()

            if  input_line.startswith('download'):
                self.download(input_line)
                continue
            elif input_line.startswith('upload') :
                self.upload(input_line)
                continue
            else:
                self.socket.sendall(bytes(input_line + "\r\n", "cp1252"))

                received = str(self.socket.recv(1024), "cp1252")
                print(received)

        self.close_socket()

    def download(self, input_line):
        if ' ' in input_line:
            file_name = input_line.split(' ', maxsplit=1)[1]
            if file_name != '':
                self.socket.sendall(bytes(input_line + "\r\n", "cp1252"))

                file_size_remaining = int.from_bytes(self.socket.recv(8), byteorder='big', signed=True)

                if file_size_remaining == -1:
                    print('файл не найден')
                    return

                file = open('./files/' + file_name, 'w+b')

                file_size = file_size_remaining
                with progressbar.ProgressBar(max_value=100) as bar:
                    while file_size_remaining != 0:
                        data = self.socket.recv(1024)
                        file.write(data)
                        file_size_remaining -= len(data)

                        bar.update(int(((file_size - file_size_remaining) / file_size)*100))

                file.close()
                print('file download')
                return
        print('input file name please')

    def upload(self, input_line):
        if ' ' in input_line:
            file_name = input_line.split(' ', maxsplit=1)[1]
            if file_name != '':
                pack_size = 1024

                try:
                    statinfo = os.stat(file_name)
                    file_size_remaining = statinfo.st_size

                    file_name_without_path =  file_name.split('/')[-1]
                    self.socket.sendall(('upload ' + file_name_without_path + ' ' + str(file_size_remaining) + "\r\n").encode('cp1252'))

                    file = open(file_name, 'rb')

                    self.socket.recv(1024) #sync

                    file_size = file_size_remaining
                    with progressbar.ProgressBar(max_value=100) as bar:
                        while file_size_remaining != 0:
                            if file_size_remaining < pack_size:
                                pack_size = file_size_remaining

                            data = file.read(pack_size)
                            self.socket.send(data)
                            file_size_remaining -= pack_size

                            bar.update(int(((file_size - file_size_remaining) / file_size) * 100))
                    file.close()
                except FileNotFoundError:
                    print('file not faund')
                    return

                print('file send')
                return
        print('input file name please')

    def close_socket(self):
        self.socket.shutdown()
        self.socket.close()