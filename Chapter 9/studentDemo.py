def main():
    from IC_student import Student
    name = input("Enter the student's name: ")
    student = Student(name)
    student.addQuiz()
    print("The total score for %s is %d and the average is %.1f"
          % (student.getName(), student.getTotalScore(),
             student.getAverageScore()))


main()
