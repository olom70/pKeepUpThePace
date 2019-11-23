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


    def computeWeigth(self, weightIntegerPart, weightDecimalPart):
        
        return self.weight
    
    def computeBMI(self):
        return self.bBMI, self.nBMI


    def computeRMR(self):
        return self.bBMR




 