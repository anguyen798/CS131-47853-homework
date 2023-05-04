class Person:
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def __repr__(self):
        return "%s, %s" % (self._name, self._year)


class Student(Person):
    def __init__(self, name, year, major):
        super().__init__(name, year)
        self._major = major

    def __repr__(self):
        return "%s, born %d is a %s major" \
               % (self._name, self._year, self._major)


class Instructor(Person):
    def __init__(self, name, year, salary):
        super().__init__(name, year)
        self._salary = salary

    def __repr__(self):
        return "%s, born in %d has a $%.2f salary" \
               % (self._name, self._year, self._salary)
