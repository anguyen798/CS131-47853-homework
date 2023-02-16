# Read three integers from user input
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# Check if the integers are all the same
if num1 == num2 == num3:
    print("all the same")
# Check if the integers are all different
elif num1 != num2 != num3 != num1:
    print("all different")
# Otherwise, they are neither all the same nor all different
else:
    print("neither")