import socket
import pickle
import struct



class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.players= self.connect()


    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))

            return pickle.loads(self.client.recv(2048))

        except socket.error as e:
            print(e)
            return "no_conn"

class Disconnect:
    disconnect = False
    all_disconnect = False
    ready = False

    def disc(self):
         return self.disconnect

    def all_disc(self):
         return self.all_disconnect

