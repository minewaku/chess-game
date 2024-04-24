from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from widgets.board import Board
from widgets.playerInfo import PlayerInfo

class gameScene(FloatLayout):
    def __init__(self, fullscreen_width, fullscreen_height, player_1, player_2,**kwargs):
        super(gameScene, self).__init__(**kwargs)
        self.counter = 0
        self.fullscreen_width = fullscreen_width
        self.fullscreen_height = fullscreen_height

        self.player_1 = player_1
        self.player_2 = player_2

        self.player_panel_1 = PlayerInfo(player=self.player_1, background_color='#e2aa23', size_hint=(None, None), size=(((fullscreen_width - fullscreen_height) / 2) - (fullscreen_width / 32), fullscreen_height / 4), pos_hint={'center_x': (((fullscreen_width - fullscreen_height) / 2) / 2) / fullscreen_width, 'center_y': 0.8})
        self.player_panel_2 = PlayerInfo(player=self.player_2, background_color='#e2aa23', size_hint=(None, None), size=(((fullscreen_width - fullscreen_height) / 2) - (fullscreen_width / 32), fullscreen_height / 4), pos_hint={'center_x': (((fullscreen_width - fullscreen_height) / 2) / 2) / fullscreen_width, 'center_y': 0.2})

        self.board_panel = Board(player_panel_1=self.player_panel_1,
                                player_panel_2=self.player_panel_2,
                                square_size=fullscreen_height / 8, 
                                rows=8, cols=8, padding=0, spacing=0, 
                                size_hint=(None, None), size=(fullscreen_height, fullscreen_height),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.switchSide()

        self.add_widget(self.board_panel)
        self.add_widget(self.player_panel_1)
        self.add_widget(self.player_panel_2)


    def end_game(self, winner):
        Popup(title='Alert', content=Label(text=f"{winner.username} win!"), size_hint=(None, None), size=(300, 200)).open()
        self.player_panel_1.timeCounter.stop_counter()
        self.player_panel_2.timeCounter.stop_counter()
        self.restart_game()


    def restart_game(self):
        self.player_1.capturedList = []
        self.player_2.capturedList = []

        self.player_panel_1 = PlayerInfo(player=self.player_1, background_color='#e2aa23', size_hint=(None, None), size=(((self.fullscreen_width - self.fullscreen_height) / 2) - (self.fullscreen_width / 32), self.fullscreen_height / 4), pos_hint={'center_x': (((self.fullscreen_width - self.fullscreen_height) / 2) / 2) / self.fullscreen_width, 'center_y': 0.8})
        self.player_panel_2 = PlayerInfo(player=self.player_2, background_color='#e2aa23', size_hint=(None, None), size=(((self.fullscreen_width - self.fullscreen_height) / 2) - (self.fullscreen_width / 32), self.fullscreen_height / 4), pos_hint={'center_x': (((self.fullscreen_width - self.fullscreen_height) / 2) / 2) / self.fullscreen_width, 'center_y': 0.2})

        self.board_panel = Board(player_panel_1=self.player_panel_1,
                                player_panel_2=self.player_panel_2,
                                square_size=self.fullscreen_height / 8, 
                                rows=8, cols=8, padding=0, spacing=0, 
                                size_hint=(None, None), size=(self.fullscreen_height, self.fullscreen_height),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.counter = self.counter + 1
        self.switchSide()

        self.clear_widgets()
        self.add_widget(self.player_panel_1)
        self.add_widget(self.player_panel_2)
        self.add_widget(self.board_panel)
    
    
    def switchSide(self):
        if self.counter % 2 == 0:
            self.board_panel.white_player = self.player_1
            self.board_panel.black_player = self.player_2
        else:
            self.board_panel.white_player = self.player_2
            self.board_panel.black_player = self.player_1
        
        self.board_panel.turn = self.board_panel.white_player