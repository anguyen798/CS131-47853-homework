class Student:
    def __init__(self, name):
        self._name = name
        self._totalScore = 0
        self._counter = 0

    def getName(self):
        return self._name

    def addQuiz(self):
        while True:
            try:
                score = float(input("Please enter the score of a quiz"
                                    " (enter a negative score"
                                    " or a word to stop): "))
                if score < 0:
                    break
                self._totalScore = self._totalScore + score
                self._counter = self._counter + 1
            except ValueError:
                break

    def getTotalScore(self):
        return self._totalScore

    def getAverageScore(self):
        if self._counter == 0:
            print("No quizzes taken")
            return 0
        average = self._totalScore / self._counter
        return average
