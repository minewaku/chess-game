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
        self.players = []
        self.client_count = 0

    def handle_client(self, client_socket, client_address):
        print(f"Handling client at address: {client_address}")
        try:
            # Assign player based on client count
            if self.client_count == 0:
                player = Player(Side.WHITE, username="Player 1")
            else:
                player = Player(Side.BLACK, username="Player 2")

            self.players.append(player)

            if self.are_all_players_ready():
                pass

            # Send player to client
            data = pickle.dumps(player)
            client_socket.send(data)
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

            self.client_count += 1

    def are_all_players_ready(self):
        for player in self.players:  # Assume self.players is a list of Player instances
            if not player.ready:
                return False
        return True

if __name__ == '__main__':
    server = Server()
    server.start_server()
