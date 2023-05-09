from persons import *

def main() :
    student = Student("Susana Frank", 2000, "CS")
    print("%s, born in %d is a %s major"
          % (student.get_name(), student.get_year(), student.get_major()))
    instructor = Instructor("Malin Andrew", 1979, 75000)
    print("%s, born in %d has a %.2f salary"
          % (instructor.get_name(), instructor.get_year(), instructor.get_salary()))

    
main()


    # To avoid hardcoding variables if needed:
    #studentName = input("Enter the student first and last name: ")
    #studentBirthyear = input("Enter the student's birthyear in yyyy format")
    #studentMajor = input("Enter the student's major: ")
    #student = Student(studentName, studentBirthyear, studentMajor)
    