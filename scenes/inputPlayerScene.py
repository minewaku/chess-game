# create a panel that allow to type username
from scr.side import Side
from scr.logger import Logger

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

from widgets.board import Board
from widgets.playerInfo import PlayerInfo
from kivy.utils import get_color_from_hex

class inputPlayerScene(FloatLayout):
    def __init__(self, fullscreen_width, fullscreen_height, background_color, client, **kwargs):
        super(inputPlayerScene, self).__init__(**kwargs)
        self.fullscreen_width = fullscreen_width
        self.fullscreen_height = fullscreen_height
        self.player = player

        self.playerPanel = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.label = Label(text='Enter your username:', font_size='40sp', size_hint=(1, 0.5))
        self.textinput = TextInput(hint_text="Name", font_size='32sp', size_hint=(1, 0.5), multiline=False)
        self.readyButton = Button(text='READY', font_size='32sp', size_hint=(1, 0.5), background_normal='', background_color=background_color)

        self.textinput.text= self.client.player.username

        self.playerPanel.add_widget(self.label)
        self.playerPanel.add_widget(self.textinput)
        self.playerPanel.add_widget(self.readyButton)

        self.readyButton.bind(on_press=self.ready)

        self.add_widget(self.playerPanel)

    def ready(self, instance):
        self.playerPanel.remove_widget(self.readyButton)
        self.playerPanel.add_widget(Label(text='Waiting', font_size='32sp', size_hint=(1, 0.5)))


    


