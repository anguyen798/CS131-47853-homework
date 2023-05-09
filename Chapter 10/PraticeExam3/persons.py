class Person :
    def __init__(self, name, year) :
        self._name = name
        self._year = year
        
    def get_name(self) :
        return self._name
    
    def get_year(self) :
        return self._year

class Student(Person) :
    def __init__(self, name, year, major) :
        super().__init__(name, year)
        self._major = major
    
    # Uncessary Code due to inheritance from the super().__init__(name, year)
    # Which gives allows the subclasses to inherit the get_name and get_year methods
    
    #def get_name(self) :
        #return super().get_name()
        
    #def get_year(self) :
        #return super().get_year()
    
    def get_major(self) :
        return self._major

class Instructor(Person) :
    def __init__(self, name, year, salary) :
        super().__init__(name, year)
        self._salary = salary
    
    # Uncessary Code due to inheritance from the super().__init__(name, year)
    # Which gives allows the subclasses to inherit the get_name and get_year methods        
    
    #def get_name(self) :
        #return super().get_name()
        
    #def get_year(self) :
        #return super().get_year()

    def get_salary(self) :
        return self._salary
