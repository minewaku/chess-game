from kivy.uix.label import Label
from kivy.clock import Clock

class timeCounter(Label):
    def __init__(self, **kwargs):
        super(timeCounter, self).__init__(**kwargs)
        self.counter = 900
        self.update_text()
        self.timer_event = None  # Initialize timer event
        self.start_counter()


    def update_time(self, dt):
        self.counter -= 1
        self.update_text()  

        if self.counter <= 0:
            self.text = "Time's up!"
            if self.parent.parent.parent.player_1 == self.parent.parent.player:
                self.parent.parent.parent.end_game(winner=self.parent.parent.parent.player_2)
            else:
                self.parent.parent.parent.end_game(winner=self.parent.parent.parent.player_1)


    def update_text(self):
        # Convert remaining seconds to minutes and seconds
        minutes = self.counter // 60
        seconds = self.counter % 60
        self.text = "{:02}:{:02}".format(minutes, seconds)


    def start_counter(self):
        if self.timer_event is None:
            self.timer_event = Clock.schedule_interval(self.update_time, 1)  # Schedule update every second


    def stop_counter(self):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None


    def reset_counter(self):
        self.counter = 900
        self.update_text()