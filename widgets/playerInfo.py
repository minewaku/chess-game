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

from widgets.surrenderButton import surrenderButton
from widgets.timeCounter import timeCounter

class PlayerInfo(BoxLayout):
    def __init__(self, player, **kwargs):
        super(PlayerInfo, self).__init__(**kwargs)
        self.player = player
        self.orientation = 'vertical'

        self.playerName = Label(text=str(player.username), size_hint=(1, 0.5))
        self.timeCounter = timeCounter(size_hint=(1, 0.5))

        self.topPanel = BoxLayout(size_hint=(1, 0.2), orientation='horizontal')
        self.topPanel.add_widget(self.playerName)
        self.topPanel.add_widget(self.timeCounter)

        self.midlePanel = StackLayout(size_hint=(1, 0.6))
        self.surrenderButton = surrenderButton(size_hint=(1, 0.2))

        with self.canvas.before:
            # Set the background color using the Color instruction
            Color(0.886, 0.667, 0.137, 1)  # Set the RGBA color (r, g, b, a)

            # Draw a rectangle as the background using the Rectangle instruction
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Bind the update_rectangle method to the layout's size and position
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)
        self.add_widget(self.topPanel)
        self.add_widget(self.midlePanel)
        self.add_widget(self.surrenderButton)

    def update_rectangle(self, *args):
        # Update the position and size of the rectangle to match the layout
        self.rect.pos = self.pos
        self.rect.size = self.size
