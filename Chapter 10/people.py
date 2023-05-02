##
# Classes for storing various types of people.
#

# Represent a general person without additional specific properties.
#
class Person:
    def __init__(self, name, year):
        self._name = name
        self._year = year

    # Construct a new person with a name and year of birth.
    # @param name the name of the person
    # @param year the year in which the person was born
    #
    def get_information(self):
        stringinfo = "%s, %s" % (self._name, self._year)
        return stringinfo


# Write the definition of the method get information()
# @param none
# @return a string containing the details of the person
#


# Represent a student with a major.
#
class Student(Person):
    def __init__(self, name, year, major):
        super().__init__(name, year)
        self._major = major

    # @param name the name of the person
    # @param year the year in which the person was born
    # @param major the student's major
    #
    def get_information(self):
        stringinfo = "%s, born %d is a %s major" % (self._name, self._year, self._major)
        return stringinfo


# John Smith, born 1987 is a CS major
# Override the method get_information()
# @ param none
# @return a string containing the details of the student (name, year, major) 
# reuse the method get_information from the parent class
#


# Represent an instructor with a salary.
#
class Instructor(Person):
    def __init__(self, name, year, salary):
        super().__init__(name, year)
        self._salary = salary

    # Construct a new instructor with a name, year of birth and salary.
    # @param name the name of the person
    # @param year the year in which the person was born
    # @param salary the instructor's salary
    #
    def get_information(self):
        stringinfo = "%s, born in %d has a $%.2f salary" % (self._name, self._year, self._salary)
        return stringinfo
# Dave White, born in1980 has a $80000.00 salary
# Override the method get information()
# @param none
# @return a string containing the details of the person (name, year, salary) 
# reuse the method get information from the parent class
