# Question 1
fullName = input("Enter your first name, middle name and last name: ")
firstName = fullName.split()[0]
middleName = fullName.split()[1]
lastName = fullName.split()[2]
print("The initials of the name are %s %s %s" % (firstName.upper()[0], middleName.upper()[0], lastName.upper()[0]))

# Question 2
allIntegersStr = input("Type in three integers using 0-9 and seperate them by spaces: ")
# while True:
#     try:
#         allIntegersStr = input("Type in three integers using 0-9 and seperate them by spaces: ")
#         if allIntegersStr.split()[0].isdigit is False or allIntegersStr.split()[1].isdigit is False or allIntegersStr.split()[2].isdigit is False:
#             break
#     except ValueError:
#         print("Your integers were entered as %s. This format might not use 0-9 and you might have used letters.\nPlease enter again using 0-9:" % (allIntegersStr))
# while len(allIntegersStr.split()) > 3:
#     print("You entered %s integers. This format has %s integers over the limit of three" % (len(allIntegersStr.split())-3,len(allIntegersStr.split())-3))
#     allIntegersStr = input("Type in three integers using 0-9 and seperate them by spaces: ")
# while len(allIntegersStr.split()) < 3:
#     print("You entered %s integers. This format has %s integers under the limit of three" % (3 - len(allIntegersStr.split()), 3 - len(allIntegersStr.split())))
#     allIntegersStr = input("Type in three integers using 0-9 and seperate them by spaces: ")


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
    print("sum: %s" % (sum(firstInteger, secondInteger, thirdInteger)))
