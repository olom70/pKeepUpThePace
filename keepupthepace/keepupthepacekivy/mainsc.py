import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import kivy.properties as properties

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
    '''
        Screen to enter all the metrics related to a profile
    '''
    def initProfileUpdate(self, metricToSave, *args):
        '''
            Update the current Profile with the modified value
        '''
        if (metricToSave == 'heightIntegerPart'):
            valueToSave = int(self.ids.profile_height_integerpart.text)
            if (valueToSave >=0 and valueToSave <= 2):
                kivy.app.App.get_running_app().myProfile.heightIntegerPart = valueToSave

        if (metricToSave == 'activityFactor'):
            valueToSave = str(self.ids.profile_activityFactor.text)
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['1'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.SEDENTARY
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['2'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.LIGHTLYACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['3'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.MODERATELYACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['4'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.ACTIVE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['5'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.VIGOROUS
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllActivityFactors()['6'])):
                 kivy.app.App.get_running_app().myProfile.activityFactor = enumandconst.ActivityFactor.VIGOROUSLYACTIVE

            
                 

class BmI(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.ids.profile_name.text = str(App.get_running_app().myProfile.profileName)
        App.get_running_app().kbbmi = App.get_running_app().myProfile.displaybBMI()
        App.get_running_app().knbmi = App.get_running_app().myProfile.displaynBMI()

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

    #load saved profiles and instantiate the default one
    listofprofiles, myProfile = persistence.getDefaultProfileFromShelf()

    # define the properties that will be updated in the user interface
    knbmi = properties.StringProperty('0')
    kbbmi = properties.StringProperty('0')
    kbmr = properties.StringProperty('0')
    khbe1918 = properties.StringProperty('0')
    khbe1984 = properties.StringProperty('0')
    khbe1990 = properties.StringProperty('0')
    kqfp = properties.StringProperty('0')
    kefp = properties.StringProperty('0')

    # initialize a profile to test the app, if none loaded
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


    def build(self):
        '''
            build the screen manager of the app
        '''
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
    
    def doThingsBetweenScreen(self):
        '''
            actions done between the transition from one screen to another
        '''
        if (self.root.current == 'metrics'):
            self.myProfile.computeAll()
            persistence.saveprofiles()
            self.kbbmi = self.myProfile.displaybBMI()
            self.knbmi = self.myProfile.displaynBMI()
            self.kbmr = self.myProfile.displayBMR()
            self.khbe1918, self.khbe1984, self.khbe1990 = self.myProfile.displayHBE()
            self.kqfp, self.kefp = self.myProfile.displayFAT()

    def nextscreen(self):
        '''
            Navigate to the next screen of the screen manager.
            Called by the navigation widget
        '''
        self.doThingsBetweenScreen()
        self.root.current = self.root.next()
    
    def previousscreen(self):
        '''
            Navigate to the previous screen of the screen manager.
            Called by the navigation widget
        '''
        self.doThingsBetweenScreen()
        self.root.current = self.root.previous()

    
if __name__ == "__main__":

    # launch the app
    KeepUpThepaceScApp().run()