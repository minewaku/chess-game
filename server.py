import socket
import pickle
import threading

from scr.player import Player
from scr.side import Side

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 9999))
        self.server_socket.listen(2)
        self.client_connections = []
        self.players = []
        self.client_count = 0

    def handle_client(self, client_socket, client_address):
        print(f"Handling client at address: {client_address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break 
            
                if data:
                    received_data = pickle.loads(data)
                    self.handle_received_data(received_data, client_socket, client_address) 

        except Exception as e:
            print(f"Error handling client at address {client_address}: {e}")
        finally:
            client_socket.close()
            print(f"Closed connection to client at address: {client_address}")


    def start_server(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address} has been established!")

            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_handler.start()

            self.client_connections.append(client_socket)
            self.client_count += 1



    def handle_received_data(self, received_data, client_socket, client_address):

        if received_data['type'] == 'initialize_player':
            if self.client_count % 2 == 1:
                response_data = {
                                    'type': 'player', 
                                    'player': Player(Side.WHITE, "Player 1")
                                }
                self.players.append(response_data['player'])

            else: 
                response_data = {
                                    'type': 'player', 
                                    'player': Player(Side.BLACK, "Player 2")
                                }
                self.players.append(response_data['player'])
                
            if len(self.players) == 2:
                response_data = {
                                    'type': 'player_list',
                                    'player_list': self.players
                                }
                self.handle_response_data_all(response_data)

            if self.client_count == 2:
                response_data = {
                                    'type': 'start_game'
                                }
                self.handle_response_data(response_data, client_socket, client_address)
            
        self.handle_response_data(response_data, client_socket, client_address)


    def handle_response_data(self, data, client_socket, client_address):
        response_data = pickle.dumps(data)
        client_socket.send(response_data)


    def handle_response_data_all(self, data):
        response_data = pickle.dumps(data)
        for client_socket in self.client_connections:
            client_socket.send(response_data)        

if __name__ == '__main__':
    server = Server()
    server.start_server()
