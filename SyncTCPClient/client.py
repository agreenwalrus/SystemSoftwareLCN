import socket
import sys


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
                self.socket.sendall(bytes(input_line + "\r\n", "cp1252"))

                #create file
                file = open('./files/temp.txt', 'w+b')
                data = self.socket.recv(1024)
                file.write(data)

                while len(data) == 1024:
                    data = self.socket.recv(1024)
                    file.write(data)

                file.close()
            elif input_line.startswith('upload') :
                upload = 1
            else:
                self.socket.sendall(bytes(input_line + "\r\n", "cp1252"))

                received = str(self.socket.recv(1024), "cp1252")
                print(received)

