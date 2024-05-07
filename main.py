from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from scr.player import Player
from scr.side import Side
from scenes.gameScene import gameScene
import socket
import threading

class Main(App): 
    def build(self):
        Window.size = (700, 700)

        player_name = input("Enter your name: ")
        # Gửi tên người chơi đến máy chủ
        client_socket.send(player_name.encode())

        player_1_name = player_name
        # Nhận tên của người chơi thứ hai từ máy chủ
        player_2_name = client_socket.recv(1024).decode()

        player_1 = Player(Side.WHITE, player_1_name)
        player_2 = Player(Side.BLACK, player_2_name)

        game_scene = gameScene(fullscreen_width=600, fullscreen_height=600, player_1=player_1, player_2=player_2)

        root = FloatLayout()
        root.add_widget(game_scene)

        return root

def receive_name():
    while True:
        player_2_name = client_socket.recv(1024).decode()
        if player_2_name:
            break
    return player_2_name

if __name__ == '__main__':
    # Kết nối tới máy chủ
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    threading.Thread(target=receive_name).start()

    Main().run()
