from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from scr.player import Player
from scr.side import Side

from scenes.gameScene import gameScene
from scenes.inputPlayerScene import inputPlayerScene

class Main(App):
    def __init__(self, client, **kwargs):
        super().__init__(**kwargs)
        self.client = client

    def build(self):
        Window.fullscreen = True
        fullscreen_height = Window.system_size[1]
        fullscreen_width = Window.system_size[0]

        player_1 = Player(Side.WHITE, "Player 1")
        player_2 = Player(Side.BLACK, "Player 2")

        background_color = '#e2aa23'
        
        self.game_scene = gameScene(fullscreen_width=fullscreen_width, fullscreen_height=fullscreen_height, background_color=background_color, player_1=player_1, player_2=player_2)
        
        self.input_user = inputPlayerScene(fullscreen_width=fullscreen_width, fullscreen_height=fullscreen_height, background_color=background_color, client=self.client,size_hint=(1, 1))
        
        root = FloatLayout()
        root.add_widget(self.input_user)
        return root

if __name__ == '__main__':
    Main().run()