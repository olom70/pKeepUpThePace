import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
import lang
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import keepupthepace.profilem.profile as profile
import keepupthepace.profilem.enumandconst as enumandconst
import keepupthepace.persistence.profilepersistence as persistence

tr = lang.Lang("en")

class RmR(BoxLayout):
    pass

class Front1(PageLayout):
    '''
        Main User Interface of the application
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.profile_name.text = str(myProfile.profileName)
        self.ids.profile_height_integerpart.text = str(myProfile.heightIntegerPart)
        self.ids.profile_height_decimalpart.text = str(myProfile.heightDecimalPart)
        self.ids.profile_weight_integerpart.text = str(myProfile.weightIntegerPart)
        self.ids.profile_weight_decimalpart.text = str(myProfile.weightDecimalPart)
        self.ids.profile_age.text = str(myProfile.age)

    def displayBMI(self):
        try:
            myProfile.computeBMI()
            self.ids.bmi_value_old_formula.text = str(myProfile.bBMI)
            self.ids.bmi_value_new_formula.text = str(myProfile.nBMI)
        except ValueError:
            self.ids.bmi_value_old_formula.text = 'not enough values'
            self.ids.bmi_value_new_formula.text = 'not enough values'

    def save(self):
        myProfile.profileName = str(self.ids.profile_name.text)
        persistence.saveprofiles()



class KeepUpThepaceApp(App):
    '''
        Main Class to launch the App
    '''
    # set the language of the app
    lang = kivy.properties.StringProperty(tr.lang)

    def on_lang(self, instance, lang):
        lang.tr.switch_lang(lang)


    # Launch the user interface
    def build(self):
        return Front1()
    
if __name__ == "__main__":

    #load saved profiles and instantiate the default one
    listofprofiles, myProfile = persistence.getDefaultProfileFromShelf()


    # initialize a profile to test the app
    if not(isinstance(myProfile, profile.Profile)):
        myProfile=profile.Profile('not coming from shelf')
        myProfile.isdefault = True
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