from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from widgets.playerInfo import PlayerInfo
from scr.player import Player
from scr.side import Side

from widgets.board import Board
from widgets.playerInfo import PlayerInfo
from scenes.gameScene import gameScene

class Main(App):
    def build(self):
        Window.fullscreen = True
        fullscreen_height = Window.system_size[1]
        fullscreen_width = Window.system_size[0]

        player_1=Player(Side.WHITE, "Player 1")
        player_2=Player(Side.BLACK, "Player 2")
        
        game_scene = gameScene(fullscreen_width=fullscreen_width, fullscreen_height=fullscreen_height, player_1=player_1, player_2=player_2)
        
        root = FloatLayout()
        root.add_widget(game_scene)
        return root

if __name__ == '__main__':
    Main().run()