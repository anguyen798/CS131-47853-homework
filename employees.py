class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return "%s has a salary of %.2f" % (self._name, self._salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return "%s has a salary of %.2f and manages the %s department" % (self._name, self._salary, self._department)


class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return "%s has a salary of %.2f and is executive for the %s department" \
            % (self._name, self._salary, self._department)
