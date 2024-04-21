from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from widgets.playerInfo import PlayerInfo
from scr.player import Player
from scr.side import Side
from kivy.uix.label import Label
from widgets.board import Board

class Main(App):
    def build(self):
        Window.fullscreen = True
        fullscreen_height = Window.system_size[1]

        # window_height = 600
        # window_width = 920
        # Window.size = (window_width, window_height)

        root = FloatLayout()

        board_panel = Board(player1=Player(Side.WHITE, "Player 1"), 
                            player2=Player(Side.BLACK, "Player 2"), 
                            square_size=fullscreen_height / 8, 
                            rows=8, cols=8, padding=0, spacing=0, 
                            size_hint=(None, None), size=(fullscreen_height, fullscreen_height),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        root.add_widget(board_panel)
        return root

if __name__ == '__main__':
    Main().run()