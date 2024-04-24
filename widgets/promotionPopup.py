import os

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

from scr.piece import Queen
from scr.piece import Horse
from scr.piece import Bishop
from scr.piece import Rook
from scr.side import Side

class promotionPopup(FloatLayout):
    def __init__(self, square, **kwargs):
        super(promotionPopup, self).__init__(**kwargs)
        self.square = square
        self.choose_pieces_panel = StackLayout(size_hint=(None, None), size=(512, 128), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.overlay_panel = StackLayout(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, disabled=True)

        with self.choose_pieces_panel.canvas.before:
            Color(0.9, 0.24, 0.24, 1)
            self.choose_pieces_panel.rect = Rectangle(pos=self.pos, size=self.size)
        self.choose_pieces_panel.bind(pos=self.update_rectangle, size=self.update_rectangle)

        queenButton = Button(size_hint=(None, None), size=(128, 128), on_press=self.select_piece)
        queenButton.id = 'queen'

        horseButton = Button(size_hint=(None, None), size=(128, 128), on_press=self.select_piece)
        horseButton.id = 'horse'

        bishopButton = Button(size_hint=(None, None), size=(128, 128), on_press=self.select_piece)
        bishopButton.id = 'bishop'

        rookButton = Button(size_hint=(None, None), size=(128, 128), on_press=self.select_piece)
        rookButton.id = 'rook'

        if square.point.piece.side == Side.WHITE:
            queenButton.background_normal=os.path.join("assets", "img", "pieces", "white_queen.png")
            horseButton.background_normal=os.path.join("assets", "img", "pieces", "white_horse.png")
            bishopButton.background_normal=os.path.join("assets", "img", "pieces", "white_bishop.png")
            rookButton.background_normal=os.path.join("assets", "img", "pieces", "white_rook.png")

        elif square.point.piece.side == Side.BLACK:
            queenButton.background_normal=os.path.join("assets", "img", "pieces", "black_queen.png")
            horseButton.background_normal=os.path.join("assets", "img", "pieces", "black_horse.png")
            bishopButton.background_normal=os.path.join("assets", "img", "pieces", "black_bishop.png")
            rookButton.background_normal=os.path.join("assets", "img", "pieces", "black_rook.png")

        self.choose_pieces_panel.add_widget(queenButton)
        self.choose_pieces_panel.add_widget(horseButton)
        self.choose_pieces_panel.add_widget(bishopButton)
        self.choose_pieces_panel.add_widget(rookButton)

        self.add_widget(self.overlay_panel)
        self.add_widget(self.choose_pieces_panel)


    def select_piece(self, instance):
        # Get the ID of the selected button
        selected_id = instance.id
        # Determine which piece to promote to based on the button ID
        if selected_id == 'queen':
            self.square.point.piece = Queen(side=self.square.point.piece.side)
        elif selected_id == 'horse':
            self.square.point.piece = Horse(self.square.point.piece.side)
        elif selected_id == 'bishop':
            self.square.point.piece = Bishop(self.square.point.piece.side)
        elif selected_id == 'rook':
            self.square.point.piece = Rook(self.square.point.piece.side)
        else:
            return
        
        self.parent.board_panel.renderVisual()
        self.dismiss()

    def update_rectangle(self, *args):
        self.choose_pieces_panel.rect.pos = self.choose_pieces_panel.pos
        self.choose_pieces_panel.rect.size = self.choose_pieces_panel.size

    #dismiss popup
    def dismiss(self):
        self.parent.remove_widget(self)
    

