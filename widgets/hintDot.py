from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class HintDot(Widget):
    # belonging to square, just a fucking dot that located at the center of each Square
    def __init__(self, **kwargs):
        super(HintDot, self).__init__(**kwargs)
        self.create_dot(color=(0.9, 0.24, 0.24, 0))

    def create_dot(self, color):
        with self.canvas:
            Color(*color)
            self.dot = Ellipse(pos=self.pos, size=self.size)

    def showHint(self):
        self.canvas.clear()
        self.create_dot(color=(0.9, 0.24, 0.24, 0.6))
        
    def hideHint(self):
        self.canvas.clear()
        self.create_dot(color=(0.9, 0.24, 0.24, 0))
