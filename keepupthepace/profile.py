
ActivityFactor = ('sedentary', 'lightlyActive', 'active', 'moderatelyActive', 'vigorous', 'vigorouslyActive')
RmrDates = ('a1918', 'a1984', 'a1990')
MetricChoice = ('iso', 'imperial')
Gender = ('Female', 'Male')

class Profile:
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
        



 