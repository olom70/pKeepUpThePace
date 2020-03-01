import abc

class Compendium(abc.ABC):
    '''
        ** abstract class **
        provides the mean to print and get the values of a domain (bicycling, Dancing, Home Activity, etc.)
    '''
    def __init__(self):
        self.metDescription_fr = {}
        self.metDescription = {}
        self.metValue = {}
    
    def printValues(self):
        for key, value in self.metValue.items():
            print({key},":",{value})

        for key, value in self.metDescription.items():
            print({key},":",{value})

        for key, value in self.metDescription_fr.items():
            print({key},":",{value})

    def getMetValue(self, code):
        try:
            return self.metValue[code]
        except (KeyError):
            raise ValueError("The met code :  "+str(code)+" is unknown.")
            
        
        
