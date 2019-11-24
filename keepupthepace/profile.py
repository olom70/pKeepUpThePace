from switch_case import *

class Profile:
    '''
        This class holds :
        - all the characteristics of a person (age, weigth, etc.)
        - and the infered metrics (BMI, RMR, etc.)
        - the activity factor ( do I lay all day long or do I have multiple physical activities ?)
    '''
    def __init__(self, profileName='a profile'):
        self.profileName = profileName
        self.maleSign = '♂'
        self.femaleSign = '♀'
        # facts
        self.fileName = None #String
        self.profileGoal = None #string
        self.metricChoice = None #from the tuple MetricChoice
        self.defaultProfile = False
        self.weight = None # float 
        self.weightIntegerPart = None
        self.weightDecimalPart = None
        self.heightIntegerPart = None
        self.heightDecimalPart = None
        self.age = None
        self.chest = None
        self.abdomen = None
        self.thigh = None
        self.triceps = None
        self.suprailium = None
        self.gender = None # from the tuple Gender
        self.activityFactor = None # from the tuple Activity Factor
        # infered
        self.bBMI = None # classic way to calculate it
        self.nBMI = None # new way to calculate it
        self.bBMR = None
        self.rRMRcal = None
        self.rRMRml = None
        self.hHBE = None
        self.quadraticBodyDensity = None
        self.exponentialBodyDensity = None
        self.quadraticFatPercentage = None
        self.exponentialFatPercentage = None


    def computeWeigth(self):
        '''
            Add the decimal part of the weight to the integer part to obtain une number
        '''
        if (self.weightDecimalPart is not None
                and self.weightIntegerPart is not None
                and self.weightDecimalPart != 0):
            self.weight = self.weightIntegerPart + (self.weightDecimalPart / 100)
        else:
            raise("weight has to be initialized first")
    
    def computeBMI(self):
        '''
            Compute BMI from weight and height of a person
            
            classic way
                http://www.bmi-calculator.net/bmi-formula.php
                Imperial : BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
                ISO : BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
            new way
                https://www.medicalnewstoday.com/articles/255712.php
                ISO: BMI = 1.3 x weight (kg) / height (m)2.5
                or
                imperial : BMI = 5734*weight(lb)/height(in)2.5
        '''
        self.computeWeigth
        if (self.weight is not None
                and self.heightIntegerPart is not None
                and self.heightDecimalPart is not None
                and self.metricChoice is not None):
            # yet to code
            gapholder = 3.14
        else:
            raise("Profile has to be fully initialized with weight, height and metric choice (iso, imperial)")


        return self.bBMI, self.nBMI    

    def computeRMR(self):
        return self.bBMR




 