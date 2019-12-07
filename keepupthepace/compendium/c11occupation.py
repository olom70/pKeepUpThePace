import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import keepupthepace.compendium.abstractcompendium

class Occupation(keepupthepace.compendium.abstractcompendium.Compendium):

    def __init__(self):
        self.metValue  = {
        
        }


        self.metDescription  = {

        }

        self.metDescription_fr  = {

        }        

    def printValues(self):
        print("Beginning dump for 'Occupation' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Occupation()
    b.printValues()
    print(b.getMetValue(2205))