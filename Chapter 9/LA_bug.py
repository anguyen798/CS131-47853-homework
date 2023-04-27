class Bug:
    def __init__(self, initialPosition):
        self._initialPosition = initialPosition
        self._move = 1

    def turn(self):
        self._move = self._move * -1

    def move(self):
        self._initialPosition = self._initialPosition + self._move

    def getPosition(self):
        return self._initialPosition
