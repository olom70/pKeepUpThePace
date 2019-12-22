import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
import lang

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import keepupthepace.profilem.profile as profile
import keepupthepace.profilem.enumandconst as enumandconst


tr = lang.Lang("en")

class Front1(PageLayout):
    pass    

class KeepUpThepaceApp(App):
    '''
        main Class to launch the App
    '''
    lang = kivy.properties.StringProperty(tr.lang)

    def on_lang(self, instance, lang):
        lang.tr.switch_lang(lang)

    def build(self):
        return Front1()
    

if __name__ == "__main__":

    # initialize a profile to test the app
    myProfile=profile.Profile()
    myProfile.age = 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weightIntegerPart = 60
    myProfile.weightDecimalPart = 0
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    myProfile.computeBMI()

    # launch the app
    KeepUpThepaceApp().run()