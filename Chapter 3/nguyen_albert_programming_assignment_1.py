# Question 1
fullName = input("Enter your first name, middle name and last name: ")
firstName = fullName.split()[0]
middleName = fullName.split()[1]
lastName = fullName.split()[2]
print("The initials of the name are %s %s %s" % (firstName.upper()[0], middleName.upper()[0], lastName.upper()[0]))

# Question 2

# allIntegersStr exception handling using if statements
while True:
    allIntegersStr = input("Type in 3 integers using 0-9 digits and separate them by spaces: ")
    if not all(i.isdigit() for i in allIntegersStr.split()):
        print("You entered %s. This uses letters and not the required 0-9 digits."
              "\nPlease enter again using 0-9:" % allIntegersStr)
    elif len(allIntegersStr.split()) > 3:
        print("You entered %s. The count is %s integers. This is %s integers over the count requirement of 3." %
              (allIntegersStr, len(allIntegersStr.split()), len(allIntegersStr.split()) - 3))
    elif len(allIntegersStr.split()) < 3:
        print("You entered %s. The count is %s integers. This is %s integers under the count requirement of 3." %
              (allIntegersStr, len(allIntegersStr.split()), 3 - len(allIntegersStr.split())))
    elif all(i.isdigit() for i in allIntegersStr.split()):
        break

firstInteger = int(allIntegersStr.split()[0])
secondInteger = int(allIntegersStr.split()[1])
thirdInteger = int(allIntegersStr.split()[2])
if firstInteger == secondInteger and secondInteger == thirdInteger and thirdInteger == firstInteger:
    print("sum: 0")
elif firstInteger != secondInteger and firstInteger != thirdInteger and secondInteger == thirdInteger:
    print("sum: %s" % firstInteger)
elif secondInteger != firstInteger and secondInteger != thirdInteger and firstInteger == thirdInteger:
    print("sum: %s" % secondInteger)
elif thirdInteger != firstInteger and thirdInteger != secondInteger and firstInteger == secondInteger:
    print("sum: %s" % thirdInteger)
else:
    print("sum: %s" % (firstInteger + secondInteger + thirdInteger))
