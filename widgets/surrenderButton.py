from kivy.uix.button import Button

class surrenderButton(Button):

    
    def __init__(self, **kwargs):
        super(surrenderButton, self).__init__(**kwargs)

        self.text = "Surrender"
        self.disabled = True


    def disabled(self):
        self.disabled = True


    def enabled(self):
        self.disabled = False


    