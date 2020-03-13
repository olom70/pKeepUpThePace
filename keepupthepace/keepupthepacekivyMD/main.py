import kivy
kivy.require('1.11.1')
import lang
import os
import sys
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.behaviors import FocusBehavior
import kivy.properties as properties
from kivy.uix.boxlayout import BoxLayout

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

class KeepUpThePaceMD(BoxLayout):
    pass

class KeepUpThePaceMDApp(MDApp):
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

    listOfMetTables = [tr._('01-Bicycling'), 
            tr._('02-Conditionning Exercises'),
            tr._('03-Dancing'),
            tr._('04-Fishing & Hunting'),
            tr._('05-Home Activity'),
            tr._('06-Home Repair'),
            tr._('07-Inactivity'),
            tr._('08-Lawn Garden'),
            tr._('09-Miscellaneous'),
            tr._('10-Music Playing'),
            tr._('11-Occupation'),
            tr._('12-Runing'),
            tr._('13-Self Care'),
            tr._('14-Sexual Activity'),
            tr._('15-Sports'),
            tr._('16-Transportation'),
            tr._('17-Walking'),
            tr._('18-Water Activities'),
            tr._('19-Winter Activities'),
            tr._('20-Religious Activities'),
            tr._('21-Volunteer Activities')]

    def build(self):
        pass

if __name__ == "__main__":

    # launch the app
    KeepUpThePaceMDApp().run()