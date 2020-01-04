import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.boxlayout import BoxLayout
import lang
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import keepupthepace.profilem.profile as profile
import keepupthepace.profilem.enumandconst as enumandconst
import keepupthepace.persistence.profilepersistence as persistence

tr = lang.Lang("en")

class Welcome(Screen):
    pass

class Overview(Screen):
    pass

class Metrics(Screen):
    pass

class BmI(Screen):
    pass

class RmR(Screen):
    pass

class TtE(Screen):
    pass

class ProfileManager(Screen):
    pass

class Settings(Screen):
    pass

class Navigation(BoxLayout):
    pass

class KeepUpThepaceScApp(App):
    '''
        Main Class to launch the App
    '''
    # set the language of the app
    lang = kivy.properties.StringProperty(tr.lang)

    def on_lang(self, instance, lang):
        lang.tr.switch_lang(lang)


    # Launch the user interface
    def build(self):
        root = ScreenManager(transition=FadeTransition())
        root.add_widget(Welcome(name='welcome'))
        root.add_widget(Overview(name='overview'))
        root.add_widget(Metrics(name='metrics'))
        root.add_widget(BmI(name='bmi'))
        root.add_widget(RmR(name='rmr'))
        root.add_widget(TtE(name='tte'))
        root.add_widget(ProfileManager(name='profilemanager'))
        root.add_widget(Settings(name='settings'))
        return root

    def nextscreen(self):
        self.root.current = self.root.next()
    
    def previousscreen(self):
        self.root.current = self.root.previous()

    
if __name__ == "__main__":

    # launch the app
    KeepUpThepaceScApp().run()