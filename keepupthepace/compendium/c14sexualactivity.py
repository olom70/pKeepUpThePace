import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import keepupthepace.compendium.abstractcompendium

class SexualActivity(keepupthepace.compendium.abstractcompendium.Compendium):

    def __init__(self):
        self.metValue  = {14010 : 2.8
            ,14020 : 1.8
            ,14030 : 1.3 }

        self.metDescription  = {14010 : "active, vigorous effort"
            ,14020 : "general, moderate effort"
            ,14030 : "passive, light effort, kissing, hugging"}

        self.metDescription_fr  = {14010 : "mode actif, effort vigoureux"
            ,14020 : "général, effort modéré"
            ,14030 : "mode passif, effort léger, baisers, embrassades"}

    def printValues(self):
        print("Beginning dump for 'SexualActivity' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = SexualActivity()
    b.printValues()
    print(b.getMetValue(14020))