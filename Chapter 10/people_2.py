##
# Classes for storing various types of people.
#

# Represent a general person without additional specific properties.
#
class Person:
    # Construct a new person with a name and year of birth.
    # @param name the name of the person
    # @param year the year in which the person was born
    #            
    def __init__(self, name, birthYear):
        self._name = name 
        self._bYear = birthYear
        
    # Write the definition of the method get information() 
    # @param none
    # @return a string containing the details of the person
    #    
    def getInfo(self): 
        print(self._name, self._bYear)



# Represent a student with a major.
#
class Student (Person):
    # Construct a new student with a name, year of birth and major.
    # @param name the name of the person
    # @param year the year in which the person was born
    # @param major the student's major
    #    
    def __init__(self, name, birthYear, major): 
        super().__init__(name, birthYear) 
        self._major = major
    # Override the method get_information()
    # @ param none
    # @return a string containing the details of the student (name, year, major) 
    # reuse the method get_information from the parent class
    #
    def getInfo(self):
        print(self._name + ",","born in", self._bYear, "is a", self._major, "major") 
        

# Represent an instructor with a salary.
#
class Instructor(Person):
    # Construct a new instructor with a name, year of birth and salary.
    # @param name the name of the person
    # @param year the year in which the person was born
    # @param salary the instructor's salary
    #
    def __init__(self, name, birthYear, salary): 
        super().__init__(name, birthYear) 
        self._salary = salary
        
    # Override the method get information()
    # @param none
    # @return a string containing the details of the person (name, year, salary) 
    # reuse the method get information from the parent class 
    #
    def getInfo(self): 
        print(self._name + ",", "born in", self._bYear, "has a", "$" + self._salary +".00", "salary") 


