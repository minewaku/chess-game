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
from kivy.utils import get_color_from_hex

from widgets.surrenderButton import surrenderButton
from widgets.timeCounter import timeCounter

class PlayerInfo(BoxLayout):
    def __init__(self, player, background_color, **kwargs):
        super(PlayerInfo, self).__init__(**kwargs)
        self.player = player
        self.orientation = 'vertical'

        self.playerName = Label(text=str(player.username), size_hint=(1, 0.5), font_size = '18sp', bold=True)
        self.timeCounter = timeCounter(size_hint=(1, 0.5), font_size = '18sp', bold=True)

        self.topPanel = BoxLayout(size_hint=(1, 0.2), orientation='horizontal')
        self.topPanel.add_widget(self.playerName)
        self.topPanel.add_widget(self.timeCounter)

        self.capturedPanel = StackLayout(size_hint=(1, 0.6))
        self.surrenderButton = surrenderButton(size_hint=(1, 0.2), font_size='18sp', bold=True, background_color='#E63D3D', background_color_on_press='#5B5C5F', background_color_on_release='#E63D3D', background_normal='', color=(1, 1, 1, 0.7), disabled_color=(1, 1, 1, 0.7))

        with self.canvas.before:
            # Set the background color using the Color instruction
            # Color(0.886, 0.667, 0.137, 1)  # Set the RGBA color (r, g, b, a)
            Color(*get_color_from_hex(background_color))
            # Draw a rectangle as the background using the Rectangle instruction
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Bind the update_rectangle method to the layout's size and position
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)
        self.add_widget(self.topPanel)
        self.add_widget(self.capturedPanel)
        self.add_widget(self.surrenderButton)

    def update_rectangle(self, *args):
        # Update the position and size of the rectangle to match the layout
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_captured_panel(self):
        if self.player.side == Side.WHITE:
            self.capturedPanel.clear_widgets()
            for item in self.player.capturedList:
                self.capturedPanel.add_widget(Image(source=item.blackImg, size_hint=(None, None), size=(32, 32)))
                print(item)

        elif self.player.side == Side.BLACK:
            self.capturedPanel.clear_widgets()
            for item in self.player.capturedList:
                self.capturedPanel.add_widget(Image(source=item.whiteImg, size_hint=(None, None), size=(32, 32)))
                print(item)