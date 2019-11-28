import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import keepupthepace.enumandconst as enumandconst
import math

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
            Add the decimal part of the weight to the integer part to obtain one number
        '''
        if (self.weightDecimalPart is not None
                and self.weightIntegerPart is not None):
            self.weight = self.weightIntegerPart + (self.weightDecimalPart / 100)
        else:
            raise ValueError("weight has to be initialized first")
    
    def __computeBMIISO(self):
        '''
            Compute the BMI from ISO metrics
            This is a private function called by "ComputeBMI"
            There are 2 formulas to compute the BMI :
                see the main function "Compute BMI"
        '''
        self.bBMI = 10000 * (self.weight / math.pow((self.heightIntegerPart*100+self.heightDecimalPart),2))  
        self.nBMI = 100000 * (self.weight*1.3 / math.pow((self.heightIntegerPart*100+self.heightDecimalPart),2.5))

    def __computeBMIImperial(self):
        '''
            Compute the BMI from imperial metrics
            This is a private function called by "ComputeBMI"
            There are 2 formulas to compute the BMI :
                see the main function "Compute BMI"
        '''
        self.bBMI = 10000*(self.weight / math.pow((self.heightIntegerPart*12+self.heightDecimalPart),2))*703
        self.nBMI = 5734*self.weight / math.pow(self.heightIntegerPart*12+self.heightDecimalPart,2.5)


    def displaynBMI(self):
        '''
            Trunc the new BMI to the nearest integer
        '''
        if self.nBMI is not None:
            truncatednBMI = math.trunc(self.nBMI)
            return truncatednBMI
        else:
            raise ValueError("In order to display nBMI, it needs initialization first")

    
    def displaybBMI(self):
        '''
            Trunc the classic BMI to the nearest integer
        '''
        if self.bBMI is not None:
            truncatedbBMI = math.trunc(self.bBMI)
            return truncatedbBMI
        else:
            raise ValueError("In order to display bBMI, it needs initialization first")


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
        try:
            self.computeWeigth()
        except:
            raise
        
        if (self.weight is not None
                and self.heightIntegerPart is not None
                and self.heightDecimalPart is not None
                and self.metricChoice is not None
                and self.metricChoice in enumandconst.MetricChoice):
            if (self.metricChoice == enumandconst.MetricChoice.ISO):
                self.__computeBMIISO()
            if (self.metricChoice == enumandconst.MetricChoice.IMPERIAL):
                self.__computeBMIImperial()
        else:
            raise ValueError("Profile has to be fully initialized with weight, height and metric choice (iso, imperial)")


        return self.bBMI, self.nBMI

    def computeRMR(self, version):
        '''
            compute the RMR.
             input :
             version : formula to use taken from the enumeration "RmrDates"
        '''
        return self.bBMR


if __name__ == "__main__":
    myProfile = Profile('clode')
    myProfile.age = 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weightIntegerPart = 60
    myProfile.weightDecimalPart = 0
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    myProfile.computeBMI()
    print(myProfile.nBMI)
    print(myProfile.bBMI)
    print(myProfile.displaybBMI())

 