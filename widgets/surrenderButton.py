from kivy.uix.button import Button

class surrenderButton(Button):

    
    def __init__(self, background_color_on_press, background_color_on_release, **kwargs):
        super(surrenderButton, self).__init__(**kwargs)

        self.background_color_on_press = background_color_on_press
        self.background_color_on_release = background_color_on_release
        
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)

        self.text = "Surrender"
        self.disabled = True

    def on_button_press(self, instance):
        self.background_color = self.background_color_on_press


    def on_button_release(self, instance):
        self.background_color = self.background_color_on_release

    

        


    