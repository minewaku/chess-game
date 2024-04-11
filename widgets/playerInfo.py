from kivy.uix.button import Button
import sys
sys.path.append('../')
from scr.side import Side
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class PlayerInfo(BoxLayout):
    def __init__(self, player, window_w, window_h, **kwargs):
        super(PlayerInfo, self).__init__(**kwargs)
        self.player = player
        self.player.username = str(self.size_hint) + " " + str(self.height) 
        self.orientation = 'vertical'
        with self.canvas.before:
            Color(0.8, 0.2, 0.2, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        name_label = Label(text=self.player.username + "(" + str(window_w) + "," + str(window_h) + ")", size_hint=(1, 0.3))
        capturedPieces = StackLayout(size_hint=(1, 0.7))
        self.add_widget(name_label)
        self.add_widget(capturedPieces)

    def updateCapturedPanel(self, piece):
        if(self.player.side == Side.WHITE):
            self.capturedPieces.add_widget(Image(source=piece.whiteImg, size_hint=(0.05, 0.05)))
        if(self.player.side == Side.BLACK):
            self.capturedPieces.add_widget(Image(source=piece.blackImg, size_hint=(0.05, 0.05)))

    def update_border(self, *args):
        # Update the border size and position
        self.border.pos = self.pos
        self.border.size = self.size

    def update_border(self, *args):
        # Update the border size and position
        self.border.pos = self.pos
        self.border.size = self.size

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size