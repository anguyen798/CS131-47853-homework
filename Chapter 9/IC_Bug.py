class Bug: 
    def __init__(self, initialPosition):
        self._start = initialPosition
        self._currentPosition = 1.0

    def turn(self):
        self._start = -abs(self._start)
        return self._start
    def move(self):
        finalPosition = 0.0
        positiveNumber = 1.0
        negativeNumber = -abs(0.1) 
        if self._start >= 0.0: 
            finalPosition = self._start + positiveNumber
            self._start = finalPosition 
            return self._start 
        elif self._start < 0.0: 
            finalPosition = self._start + 1.0
            self._start = abs(finalPosition) 
            return self._start
    def getPosition(self): 
        return self._start
