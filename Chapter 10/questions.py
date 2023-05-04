class Question:
    def __init__(self):
        self._text = ""
        self._answer = ""

    def setText(self, questionText):
        self._text = questionText

    def checkAnswer(self, response):
        return response == self._answer

    def display(self):
        print(self._text)


class ChoiceQuestion(question):
    def __init__(self, questionText):
        super().__init__(questionText)
        self._choices = []

    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)

    def display(self):
        super().display()
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices))
