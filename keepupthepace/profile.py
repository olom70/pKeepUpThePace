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
        bBMI = None # classic way to calculate it
        nBMI = None # new way to calculate it
        bBMR = None
        rRMRcal = None
        rRMRml = None
        hHBE = None
        quadraticBodyDensity = None
        exponentialBodyDensity = None
        quadraticFatPercentage = None
        exponentialFatPercentage = None

    def computeWeigth():
        
    
    def computeBMI():
        return bBMI, nBMI

    def computeRMR():
        return bBMR




 