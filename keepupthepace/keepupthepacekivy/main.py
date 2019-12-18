import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class Front1(PageLayout):
    pass


class KeepUpThepaceApp(App):
    def build(self):
        return Front1()

if __name__ == "__main__":
    KeepUpThepaceApp().run()