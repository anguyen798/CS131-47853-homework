from employees import *


def main():
    employeeDemo = Employee("John Smith", 45000)
    managerDemo = Manager("Jane Doe", 60000, "Widgets")
    executiveDemo = Executive("Weird Guy", 90000, "Thingies")
    
    print(employeeDemo)
    print(managerDemo)
    print(executiveDemo)

main()
