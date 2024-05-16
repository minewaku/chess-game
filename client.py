from kivy.app import App
from main import Main

from scr.player import Player

import socket
import pickle

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 9999))


    def start_client(self):
        # Receive player from server
        data = self.client_socket.recv(1024)
        self.player = pickle.loads(data)
        print(f"Received player: {self.player.username}")

        self.main = Main(self)
        self.main.run()


    def send_username(client_socket, username):
        data = pickle.dumps(username)
        client_socket.send(data)
        client_socket.close()


    def send_object(client_socket, client_object):
        data = pickle.dumps(client_object)
        client_socket.send(data)
        client_socket.close()

if __name__ == '__main__':
    client = Client()
    client.start_client()

