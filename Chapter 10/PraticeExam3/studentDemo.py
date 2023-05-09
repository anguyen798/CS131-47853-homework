from IC_student import Student

def main() :
    name = input("Enter the student's name: ")
    student = Student(name)
    student.addQuiz(69.5)
    student.addQuiz(69.5)
    print("The total score for %s is %d and the average is %.1f" 
          % (student.getName(), student.getTotalScore(), student.getAverageScore()))
    
main()
