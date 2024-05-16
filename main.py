from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from scr.player import Player
from scr.side import Side

from scenes.gameScene import gameScene
from scenes.inputPlayerScene import inputPlayerScene

import socket
import pickle

class Main(App):
    def __init__(self, client, **kwargs):
        super().__init__(**kwargs)
        self.client = client
        Window.fullscreen = True
        self.fullscreen_height = Window.system_size[1]
        self.fullscreen_width = Window.system_size[0]
        self.player_list = []
        self.background_color = '#e2aa23'
        self.currentPlayer = None

    def build(self):
        # self.game_scene = gameScene(fullscreen_width=fullscreen_width, fullscreen_height=fullscreen_height, background_color=background_color, player_1=player_1, player_2=player_2)
        self.root = FloatLayout()
        return self.root
    
    def add_input_user(self):
        self.input_user = inputPlayerScene(fullscreen_width=self.fullscreen_width, fullscreen_height=self.fullscreen_height, background_color=self.background_color, client=self.client, currentPlayer=self.currentPlayer, size_hint=(1, 1))
        self.root.add_widget(self.input_user)
        print(self.currentPlayer)

    # def add_game_scene(self):
    #     self.root.add_widget(self.game_scene)
    #     self.game_scene = gameScene(fullscreen_width=self.fullscreen_width, fullscreen_height=self.fullscreen_height, background_color=self.background_color, player_1=self.player_list[0], player_2=self.player_list[1], size_hint=(1, 1))

if __name__ == '__main__':
    Main().run()