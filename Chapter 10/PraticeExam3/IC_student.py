class Student :
    def __init__(self, name) :
        self._name = name
        self._counter = 0
        self._score = 0
    
    def getName(self) :
        return self._name
    
    def addQuiz(self, score) :
        self._counter += 1
        self._score = self._score + score
    
    def getTotalScore(self) :
        return self._score
    
    def getAverageScore(self) :
        average = self._score / self._counter
        return average
        