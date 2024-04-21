from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from widgets.playerInfo import PlayerInfo
from scr.player import Player
from scr.side import Side
from kivy.uix.label import Label

from widgets.board import Board
from widgets.surrenderButton import surrenderButton
from widgets.playerInfo import PlayerInfo

class Main(App):
    def build(self):
        Window.fullscreen = True
        fullscreen_height = Window.system_size[1]
        fullscreen_width = Window.system_size[0]

        player1=Player(Side.WHITE, "Player 1")
        player2=Player(Side.BLACK, "Player 2")
        
        root = FloatLayout()

        board_panel = Board(player1=player1, 
                            player2=player2, 
                            square_size=fullscreen_height / 8, 
                            rows=8, cols=8, padding=0, spacing=0, 
                            size_hint=(None, None), size=(fullscreen_height, fullscreen_height),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
    
        playerInfo_1 = PlayerInfo(player=player1, size_hint=(None, None), size=(((fullscreen_width - fullscreen_height) / 2) - (fullscreen_width / 32), fullscreen_height / 5), pos_hint={'center_x': (((fullscreen_width - fullscreen_height) / 2) / 2) / fullscreen_width, 'center_y': 0.9})
        playerInfo_2 = PlayerInfo(player=player2, size_hint=(None, None), size=(((fullscreen_width - fullscreen_height) / 2) - (fullscreen_width / 32), fullscreen_height / 5), pos_hint={'center_x': (((fullscreen_width - fullscreen_height) / 2) / 2) / fullscreen_width, 'center_y': 0.1})

        root.add_widget(board_panel)
        root.add_widget(playerInfo_1)
        root.add_widget(playerInfo_2)
        return root

if __name__ == '__main__':
    Main().run()