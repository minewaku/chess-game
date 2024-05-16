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
        self.main = Main(self)
        self.handle_respone_data({'type': 'initialize_player'})
        data = self.client_socket.recv(1024)
        received_data = pickle.loads(data)
        self.handle_received_data(received_data)
        self.main.run()
        
        self.main.add_input_user()

        while True:
            data = self.client_socket.recv(1024)
            received_data = pickle.loads(data)
            self.handle_received_data(received_data)

    
    def handle_received_data(self, received_data):

        if received_data['type'] == 'player':
            player = received_data['player']
            self.main.player_list.append(player)
            if self.main.currentPlayer == None:
                self.main.currentPlayer = player

        elif received_data['type'] == 'player_list':
            self.main.players = received_data['player_list']


    def handle_respone_data(self, data):
        response_data = pickle.dumps(data)
        self.client_socket.send(response_data)


if __name__ == '__main__':
    client = Client()
    client.start_client()

