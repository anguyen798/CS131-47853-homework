class Car:


    def __init__(self, milesPerGallon):
        self._initialFuel = 0
        self._milesPerGallon = milesPerGallon

    def addGas(self, gallons):
        self._gasLevel = self._initialFuel + gallons
        return self._gasLevel
    
    def drive(self, miles):
        self._gasLevel = self._gasLevel - (miles / self._milesPerGallon)
        return self._gasLevel
    
    def getGasLevel(self):
        return "%.1f" % self._gasLevel
