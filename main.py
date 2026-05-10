from kivy.app import App
from kivy.uix.label import Label

class FootballApp(App):
    def build(self):
        return Label(text="Football App Works!")

FootballApp().run()
