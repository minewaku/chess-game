import sys

from scr.side import Side
from scr.piece import Piece

from .hintDot import HintDot 

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class Square(FloatLayout):
    # each Square on board is a FloatLayout that contains a clickable Button, a HintDot and a Image

    def __init__(self, point, board, background_color, **kwargs):
        super(Square, self).__init__(**kwargs)
        self.point = point
        self.board = board
        self.background_color = background_color
        self.moveSet = []

        # self.button = Button(size_hint=(1.0, 1.0), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color = self.background_color, background_normal = '', background_down = '', on_press=lambda instance: self.on_click(turn=self.board.turn, board=self.board))
        self.button = Button(size_hint=(1.0, 1.0), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color = self.background_color, background_normal = '', background_down = '', on_press=lambda instance: self.board.selectSquare(square=self))
        self.img = Image(size_hint=(1.0, 1.0), pos_hint={'center_x': 0.5, 'center_y': 0.5}, source=Piece.transparentImg)
        self.hintDot = HintDot(size_hint=(0.25, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.button)
        self.add_widget(self.img)
        self.add_widget(self.hintDot)


    # assign the piece's image which is on the square
    def updateVisual(self):
        if self.point.piece != None:
            if self.point.piece.side == Side.BLACK:
                self.img.source = self.point.piece.blackImg

            else:
                self.img.source = self.point.piece.whiteImg

        else:
            self.img.source = Piece.transparentImg

           
        

