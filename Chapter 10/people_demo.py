from people import *
# In this module, you will create objects of the class type 
# Student and Instructor
# Follow the instructions below:

# Import the classes
# Create an object of type Student and initialize it with the following: 
# name: John Smith
# birth year: 1987
# major: CS

# Print information using the method defined in people.py module using 
# the following format:
# John Smith, born 1987 is a CS major


# Create an object of type Instructor and initialize it with the following:
# name: Dave White
# birth year: 1980
# Salary: 80000

# Print information using the method defined in people.py module using 
# the following format:
# Dave White, born in1980 has a $80000.00 salary

def main():
    studentdemo = Student("John Smith", 1987, "CS")
    print(studentdemo.get_information())
    instructordemo = Instructor("Dave White", 1980, 80000)
    print(instructordemo.get_information())


main()
