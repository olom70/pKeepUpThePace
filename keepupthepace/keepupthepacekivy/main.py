import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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
import keepupthepace.compendium.c01bicycling as c01
import keepupthepace.compendium.c02conditioningexercise as c02
import keepupthepace.compendium.c03dancing as c03
import keepupthepace.compendium.c04fishinghunting as c04
import keepupthepace.compendium.c05homeactivity as c05
import keepupthepace.compendium.c06homerepair as c06
import keepupthepace.compendium.c07inactivity as c07
import keepupthepace.compendium.c08lawngarden as c08
import keepupthepace.compendium.c09miscellaneous as c09
import keepupthepace.compendium.c10musicplaying as c10
import keepupthepace.compendium.c11occupation as c11
import keepupthepace.compendium.c12running as c12
import keepupthepace.compendium.c13selfcare as c13
import keepupthepace.compendium.c14sexualactivity as c14
import keepupthepace.compendium.c15sports as c15
import keepupthepace.compendium.c16transportation as c16
import keepupthepace.compendium.c17walking as c17
import keepupthepace.compendium.c18wateractivities as c18
import keepupthepace.compendium.c19winteractivities as c19
import keepupthepace.compendium.c20religiousactivities as c20
import keepupthepace.compendium.c21valunteeractivities as c21

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
            Update (in memory only) the current Profile with the modified value
        '''
        if (metricToSave == 'heightIntegerPart'):
            valueToSave = int(self.ids.profile_height_integerpart.text)
            if (valueToSave >=0 and valueToSave <= 2):
                kivy.app.App.get_running_app().myProfile.heightIntegerPart = valueToSave

        if (metricToSave == 'profileName'):
            valueToSave = str(self.ids.profile_name.text)
            if (len(valueToSave) > 0):
                kivy.app.App.get_running_app().myProfile.profileName = valueToSave
                 
        if (metricToSave == 'heightDecimalPart'):
            valueToSave = int(self.ids.profile_height_decimalpart.text)
            if (valueToSave >= 0 and valueToSave <= 99):
                kivy.app.App.get_running_app().myProfile.heightDecimalPart = valueToSave

        if (metricToSave == 'weightIntegerPart'):
            valueToSave = int(self.ids.profile_weight_integerpart.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.weightIntegerPart = valueToSave

        if (metricToSave == 'weightDecimalPart'):
            valueToSave = int(self.ids.profile_weight_decimalpart.text)
            if (valueToSave >= 0 and valueToSave <= 99):
                kivy.app.App.get_running_app().myProfile.weightDecimalPart = valueToSave

        if (metricToSave == 'age'):
            valueToSave = int(self.ids.profile_age.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.age = valueToSave

        if (metricToSave == 'gender'):
            valueToSave = str(self.ids.profile_gender.text)
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllGenders()['0'])):
                 kivy.app.App.get_running_app().myProfile.gender = enumandconst.Gender.FEMALE
            if (valueToSave == str(kivy.app.App.get_running_app().myProfile.getAllGenders()['1'])):
                 kivy.app.App.get_running_app().myProfile.gender = enumandconst.Gender.MALE

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

        if (metricToSave == 'femaletriceps'):
            valueToSave = int(self.ids.profile_female_triceps.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.triceps = valueToSave

        if (metricToSave == 'femalesuprailium'):
            valueToSave = int(self.ids.profile_female_suprailium.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.suprailium = valueToSave

        if (metricToSave == 'femalethigh'):
            valueToSave = int(self.ids.profile_female_thigh.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.thigh = valueToSave

        if (metricToSave == 'maletriceps'):
            valueToSave = int(self.ids.profile_male_triceps.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.triceps = valueToSave

        if (metricToSave == 'maleabdomen'):
            valueToSave = int(self.ids.profile_male_abdomen.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.abdomen = valueToSave

        if (metricToSave == 'malethigh'):
            valueToSave = int(self.ids.profile_male_thigh.text)
            if (valueToSave >= 1):
                kivy.app.App.get_running_app().myProfile.thigh = valueToSave

    def on_focus(self, focused, metricToSave):
        '''
            Triggered by TextInput.
            Is intended to save the value when the focus is lost
        '''
        if focused:
            pass
        else:
            self.initProfileUpdate(metricToSave)

class BmI(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.ids.profile_name.text = str(App.get_running_app().myProfile.profileName)
#        App.get_running_app().kbbmi = App.get_running_app().myProfile.displaybBMI()
#        App.get_running_app().knbmi = App.get_running_app().myProfile.displaynBMI()

class RmR(Screen):
    pass

class ListMetTables(Screen):
    pass

class Fat(Screen):
    pass

class ProfileManager(Screen):
    pass

class Settings(Screen):
    pass

class Navigation(FloatLayout):
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
    krmr1918 = properties.StringProperty('0')
    krmr1984 = properties.StringProperty('0')
    krmr1990 = properties.StringProperty('0')
    krmrml1918 = properties.StringProperty('0')
    krmrml1984 = properties.StringProperty('0')
    krmrml1990 = properties.StringProperty('0')
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
    else:
        myProfile.computeAll()

    # initialize all the MET tables
    bicycling = c01.Bicycling
    conditionningExercises = c02.ConditionningExercises
    dancing = c03.Dancing
    fishingHunting = c04.FishingHunting
    homeActivity = c05.HomeActivity
    homeRepair = c06.HomeRepair
    inactivity = c07.Inactivity
    lawnGarden = c08.LawnGarden
    miscellaneous = c09.Miscellaneous
    musicPlaying = c10.MusicPlaying
    occupation = c11.Occupation
    running = c12.Running
    selfcare = c13.SelfCare
    sexualActivity = c14.SexualActivity
    sports = c15.Sports
    transportation = c16.Transportation
    walking = c17.Walking
    waterActivities = c18.WaterActivities
    winterActivites = c19.WinterActivities
    religiousActivities = c20.ReligiousActivities
    volunteeractivities = c21.VolunteerActivities

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
        root.add_widget(ListMetTables(name='listmettables'))
        root.add_widget(Fat(name='fat'))
        root.add_widget(ProfileManager(name='profilemanager'))
        root.add_widget(Settings(name='settings'))
        return root

    def on_stop(self):
        persistence.saveprofiles()
    
    def doThingsBetweenScreen(self):
        '''
            actions done between the transition from one screen to another
        '''
        if (self.root.current == 'metrics' or self.root.current == 'welcome'):
            self.myProfile.computeAll()
            persistence.saveprofiles()
            self.kbbmi = self.myProfile.displaybBMI()
            self.knbmi = self.myProfile.displaynBMI()
            self.krmr1918, self.krmr1984, self.krmr1990 = self.myProfile.displayRMR()
            self.krmrml1918, self.krmrml1984, self.krmrml1990 = self.myProfile.displayRMRml()
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