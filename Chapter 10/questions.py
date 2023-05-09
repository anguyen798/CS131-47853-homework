##
# This module defines a class that models exam questions.
#

## A question with a text and an answer.
#
class Question:
    ## Constructs a question with empty question and answer strings.
    #
    def __init__(self):
        self._text = ""
        self._answer = ""

    ## Sets the question text.
    # @param questionText the text of this question
    #
    def setText(self, questionText):
        self._text = questionText

    ## Sets the answer for this question.
    # @param correctResponse the answer
    #
    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    ## Checks a given response for correctness.
    # @param response the reponse to check
    # @return True if the reponse was correct, False otherwise
    #
    def checkAnswer(self, response):
        return response == self._answer

    ## Displays this question.
    #
    def display(self):
        print(self._text)


class ChoiceQuestion(Question):
    def __init__(self, questionText):
        # Super refers to Question class, call superclass constructor first
        super().__init__(questionText)
        # Subclass constructor can contain additional statements
        self._choices = []

    # Subclass method not in super Question class
    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)

    # Overwrite super Question class.display()
    def display(self):
        super().display()
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices))
