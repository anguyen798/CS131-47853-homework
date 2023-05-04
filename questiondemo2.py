from questions import ChoiceQuestion


def main():
    first = ChoiceQuestion()
    first.setText("In what year was the Python language first released?")
    first.addChoice("1991", False)
    first.addChoice("1995", False)
    first.addChoice("1998", False)
    first.addChoice("2000", False)

    second = ChoiceQuestion()
    second.setText("In which country was the inventor of Python born?")
    second.addChoice("Australia", False)
    second.addChoice("Canada", False)
    second.addChoice("Netherlands", True)
    second.addChoice("United States", False)

    presentQuestion(first)
    presentQuestion(second)


def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))


main()
