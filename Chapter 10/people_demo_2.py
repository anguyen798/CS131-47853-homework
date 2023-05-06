# In this module, you will create objects of the class type 
# Student and Instructor
# Follow the instructions below:

# Import the classes
def main(): 
    from people import Person, Student, Instructor 
    personTest = input("Is the person an instructor or student?: ")
    personTest.lower()
    if personTest == "student":
        studentName = input("name: ")
        birthYear = input("birth year: ")
        major = input("major: ") 
        someStudent = Student(studentName, birthYear, major) 
        someStudent.getInfo()
    elif personTest == "instructor": 
        instructorName = input("name: ")
        birthYear = input("birth year: ") 
        salary = input("salary: ") 
        someInstructor = Instructor(instructorName, birthYear, salary) 
        someInstructor.getInfo()
main()
