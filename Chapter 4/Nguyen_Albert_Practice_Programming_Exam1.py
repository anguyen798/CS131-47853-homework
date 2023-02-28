# Q1
from math import sqrt
rectangleLength = int(input("Enter the length of the rectangle: "))
rectangleWidth = int(input("Enther the width of the rectangle: "))
rectangleArea = rectangleLength * rectangleWidth
rectanglePerimeter = 2 * rectangleLength + 2 * rectangleWidth
rectangleDiagonal = sqrt(rectangleLength ** 2 + rectangleWidth ** 2)

print("The area is %.1f" % rectangleArea)
print("The perimeter is %.1f" % rectanglePerimeter)
print("The diagonal length is %.2f" % rectangleDiagonal)

# Q2
string = input("Please enter a word: ")
stringLength = len(string)
stringBackwards = ""
for letter in range(stringLength):
    stringBackwards = string[letter] + stringBackwards
print(stringBackwards)

# Q3
stringQ3 = input("Enter a string: ")
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?" 
period = "."
# Check if 

if stringQ3.isalpha() and upperCase not in stringQ3:
    print("The string contains only letters")
elif stringQ3.isupper():
    print("All letters in the string are uppercase letters.")
elif stringQ3.endswith("."):
    print("The string ends with a period.")
else:
    print("The string contains a number")