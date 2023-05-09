from persons import *

def main() :
    person = Person("Good Example", 2022)
    student = Student("Susana Frank", 2000, "CS")
    instructor = Instructor("Malin Andrew", 1979, 75000)
    
    print(person.getInfo())
    print(student.getInfo())
    print(instructor.getInfo())

    
main()


    # To avoid hardcoding variables if needed:
    #studentName = input("Enter the student first and last name: ")
    #studentBirthyear = input("Enter the student's birthyear in yyyy format")
    #studentMajor = input("Enter the student's major: ")
    #student = Student(studentName, studentBirthyear, studentMajor)
    