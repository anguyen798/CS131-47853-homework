import math
# Docstrings for current exercises in enclosed in double quotes
# **************************************************
# Lab 2a


def lab_2a_print():  # To keep CONSTANTS and variables in local scope to not affect output of lab_2(a-e) code
    """
    Soft drinks are sold in cans and bottles. A store offers a six-pack of
    12-ounce cans for the same price as a two-liter bottle. \b
    Which should you buy? (1 liter is 33.814 ounces)

    You will need the following variables: \b
    List of variables \b\t\t\tType of Number \b
    Number of cans per pack \b\t\tWhole number \b
    Ounces per can \b\t\t\t\tWhole number \b
    Ounces per bottle \b\t\t\tNumber with fraction \b

    Write a program that calculates the capacity of soda in a six-pack of soda and print it. \b
    Print a statement at the end that states which is the better buy. \b
    Your program should demonstrate the use of variables and constants.
    """
    # _Prefix before CONSTANTS for PyCharm and VSCode lowercase naming warnings
    _CANS_PER_PACK = int(6)
    _OUNCES_PER_CAN = int(12)
    _OUNCES_PER_PACK = _CANS_PER_PACK * _OUNCES_PER_CAN
    _OUNCES_PER_LITER = 33.814
    _OUNCES_PER_BOTTLE_2LITER = 2 * _OUNCES_PER_LITER
    print("The ounces in a six-pack of soda = %.2f" % _OUNCES_PER_PACK)
    print("The ounces in a two-litter bottle of soda = %.2f" % _OUNCES_PER_BOTTLE_2LITER)


print("*" * 100)
print("\033[4mLAB 2A\033[0m")
lab_2a_print()
print(lab_2a_print.__doc__)

# **************************************************
# Lab 2b


def lab_2b_print(x, y):  # To keep CONSTANTS and variables in local scope to not affect output of lab_2(a-e) code
    """
Given two integers, write a program that prints \b
-The sum \b
-The difference \b
-The product \b
-The average \b
-The distance (absolute value of the difference) \b
-The maximum (the larger of the two) \b
-The minimum (the smaller of the two)\n
Hint: Python defines max and min functions that accept a sequence of values, each
separated with a comma.

Test your program with the following integers:\n
3, 8 \b
-2, 0 \b
-5, -1 \b
-4, 4 \b

    :param x:
    :param y:
    :return: None
    """
    # _Prefix before CONSTANTS for PyCharm and VSCode lowercase naming warnings
    _LAB_2B_SUM = x + y
    _LAB_2B_DIFFERENCE = x - y
    _LAB_2B_PRODUCT = x * y
    _LAB_2B_AVERAGE = (x + y) / 2
    _LAB_2B_DISTANCE = abs(x - y)
    _LAB_2B_MAXIMUM = max(x, y)
    _LAB_2B_MINIMUM = min(x, y)
    print("For x =", x, "and y =", y, ":")
    print("Sum =", _LAB_2B_SUM)
    print("Difference =", _LAB_2B_DIFFERENCE)
    print("Product =", _LAB_2B_PRODUCT)
    print("Average =", _LAB_2B_AVERAGE)
    print("Distance =", _LAB_2B_DISTANCE)
    print("Maximum =", _LAB_2B_MAXIMUM)
    print("Minimum =", _LAB_2B_MINIMUM)
    print("-" * 50)


print("*" * 100)
print("\033[4mLAB 2B\033[0m")
lab_2b_print(x=3, y=8)
lab_2b_print(x=-2, y=0)
lab_2b_print(x=-5, y=-1)
lab_2b_print(x=-4, y=4)
print(lab_2b_print.__doc__)


# lab_2b_print(x=int(input("Enter x = ")), y=int(input("Enter y = ")))  # manual input example
# **************************************************
# Lab 2c


def lab_2c_print():  # to keep x, y, a, b, c variables in local scope to not affect output of lab_2(a-e) code
    # Docstring for current exercise in enclosed in single quotes below
    """
    Find and print the result of the following 3 equations:
    x=10   y = 6     a = 2    b= 8    c = 1
    :return: None
    """
    # _Prefix before CONSTANTS for PyCharm and VSCode lowercase naming warnings
    x, y, a, b, c = 10, 6, 2, 8, 1  # assign multiple variables on one line
    _LAB_2C_SQRT = math.sqrt(x + y)
    _LAB_2C_QUADRATIC = -b + math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    _LAB_2C_EXPONENT = x ** (y + 7)
    print("For x =", x, ", y =", y, ". The square root of x + y =", _LAB_2C_SQRT,  # normal format
          "or %.2f" % _LAB_2C_SQRT)  # %f format
    print("For a =", a, ", b =", b, ", c =", c,
          ". The quadratic formula for (-b + sqrt(b^2 - 4ac)/2a =",  _LAB_2C_QUADRATIC,
          "or %-10f" % _LAB_2C_QUADRATIC,  # %f format but with left-justify and without .2f to show un-rounded value
          "or", f'{_LAB_2C_QUADRATIC:.2f}')  # f-string format
    print("For x =", x, ", y =", y, ". The formula x ^ (y + 7) =", f'{_LAB_2C_EXPONENT:,}')  # f-string format


print("*" * 100)
print("\033[4mLAB 2C\033[0m")
lab_2c_print()
print(lab_2c_print.__doc__)


# **************************************************
# Lab 2d


def lab_2d_print():
    """
    Prompt the user to enter their first name using only lowercase letters and store it into a variable,
    then prompt the user to enter their last name (also in all lowercase) and store it.
    Prompt the user to enter their age and convert it to an integer and store it.
    Concatenate your first and last name and store it in a third variable.
    Print the following:
    -a line of 50 stars (String repetition)
    -your full name by incorporating a format specifier so that your name is left-justified and uses 25 spaces
    -your full name in all caps using a string method
    -your initials (using the square brackets )
    -the length of your name (sample statement:  "the length of my full name is 12")
    -49ers (convert the number 49 to a string)
    -print how old you will be in ten years by adding
    -a line of 50 +'s
    :return: None
    """
