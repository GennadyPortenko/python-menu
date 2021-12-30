import socket


class SocketLogger:
    def __init__(self, port, enabled=True):
        self.enabled = enabled if port is not None else False

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.clientSocket.connect(("127.0.0.1", int(port)))
        except Exception as e:
            print('Logger: failed to connect to socket. Logging disabled')
            self.enabled = False

    def log(self, msg):
        if self.enabled:
            try:
                self.clientSocket.send((msg + '\n').encode())
            except Exception as e:
                print(str(e))
                self.enabled = False
