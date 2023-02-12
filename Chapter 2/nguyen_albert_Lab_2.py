# =============================================================================
# LAB 2 Import And Headings
# =============================================================================
import math
# Docstrings lines for current exercises are minimized in screenshots and enclosed in double quotes, output still shown
# Functions to keep CONSTANTS and variables in local scope to not affect output of lab_2(a-e) code
# _Prefix before CONSTANTS for PyCharm and VSCode lowercase naming warnings


def lab_2_heading(letter: str = ""):
    r"""
    Enter the string value of letter encapsulated by quotes for the LAB 2 exercise
    :param letter: lab_2_heading(letter= **letter**:str)
    :return: None
    """
    print("*" * 100)
    print(f'\033[4mLAB 2{letter}\033[0m')  # f-string with underline f'\033[4m  \033[0m'
    print("-" * 50)


# =============================================================================
# LAB 2A
# =============================================================================


def lab_2a_print(cansPerPack: int = 6, litersPerBottle: int = 2):
    r"""
    Soft drinks are sold in cans and bottles. A store offers a six-pack of
    12-ounce cans for the same price as a two-liter bottle.
    Which should you buy? (1 liter is 33.814 ounces)

    You will need the following variables:
    List of variables           Type of #
    Number of cans per pack     Whole number
    Ounces per can              Whole number
    Ounces per bottle           Number with fraction

    Write a program that calculates the capacity of soda in a six-pack of soda and print it.
    Print a statement at the end that states which is the better buy.
    Your program should demonstrate the use of variables and constants.
    :param cansPerPack: lab_2a_print(\ **cansPerPack**\:int, litersPerBottle:int)
    :param litersPerBottle: lab_2a_print(cansPerPack:int, \ **litersPerBottle**\:int)
    :return:
    """
    _OUNCES_PER_CAN = int(12)
    _OUNCES_PER_PACK = cansPerPack * _OUNCES_PER_CAN
    _OUNCES_PER_LITER = 33.814
    _OUNCES_PER_BOTTLE = litersPerBottle * _OUNCES_PER_LITER

    if cansPerPack == 6 and litersPerBottle == 2:
        print(
            f'\033[4mLab2A with default values: {cansPerPack} cans per pack'
            f'and {litersPerBottle} liters per bottle.\033[0m')
    else:
        print(
            f'\033[4mLab2A with custom values: {cansPerPack} cans per pack'
            f'and {litersPerBottle} liters per bottle.\033[0m')
    print("A", cansPerPack, "-pack of soda has %.2f" % _OUNCES_PER_PACK, "ounces")
    print("A", litersPerBottle, "-liter bottle of soda has %.2f" % _OUNCES_PER_BOTTLE, "ounces")
    if _OUNCES_PER_PACK > _OUNCES_PER_BOTTLE:
        print("You should buy the", cansPerPack, "-pack of soda because %.2f" % _OUNCES_PER_PACK,
              "ounces > the", litersPerBottle, "-liter bottle of soda with %.2f" % _OUNCES_PER_BOTTLE, "ounces")
    elif _OUNCES_PER_PACK < _OUNCES_PER_BOTTLE:
        print("You should buy the", litersPerBottle, "-liter of soda because %.2f" % _OUNCES_PER_BOTTLE,
              "ounces > the", cansPerPack, "-pack of soda  with %.2f" % _OUNCES_PER_PACK, "ounces")
    print("-" * 50)


lab_2_heading(letter="A")
lab_2a_print()
lab_2a_print(30, 5)
print(lab_2a_print.__doc__)
# =============================================================================
# LAB 2B
# =============================================================================


def lab_2b_print(x: int, y: int):
    r"""
Given two integers, write a program that prints
-The sum
-The difference
-The product
-The average
-The distance (absolute value of the difference)
-The maximum (the larger of the two)
-The minimum (the smaller of the two)

Hint: Python defines max and min functions that accept a sequence of values, each
separated with a comma.

Test your program with the following integers:
3, 8
-2, 0
-5, -1
-4, 4

    :param x: lab_2b_print(**x**, y);
    value for equations: **x** + y; **x** - y; **x** * y; (**x** + y)/2; abs(**x** - y); max(**x**,y); min(**x**, y)
    :param y: lab_2b_print(x, **y**);
    value for equations: x + **y**; x - **y**; x * **y**; (x + **y**)/2; abs(x - **y**); max(x,**y**); min(x, **y**)
    :return: None
    """
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


lab_2_heading(letter="B")
lab_2b_print(x=3, y=8)
lab_2b_print(x=-2, y=0)
lab_2b_print(x=-5, y=-1)
lab_2b_print(x=-4, y=4)
print(lab_2b_print.__doc__)
# lab_2b_print(x=int(input("Enter x = ")), y=int(input("Enter y = ")))  # manual input example
# =============================================================================
# LAB 2C
# =============================================================================


def lab_2c_print(x: int = 10, y: int = 6, a: int = 2, b: int = 8, c: int = 1):
    r"""
    Find and print the result of the following 3 equations:
    x=10
    y=6
    a=2
    b=8
    c=1
    :param x: value for equations: sqrt(**x** - y) and \ **x**\^(y + 7)
    :param y: value for equations: sqrt(x - **y**) and x^(\ **y**\ + 7)
    :param a: value for equation: (-b + sqrt(b^2 - 4\ **a**\ c)/2\ **a**\
    :param b: value for equation: (-**b** + sqrt(\ **b**\ ^2 - 4ac)/2a
    :param c: value for equation: (-b + sqrt(b^2 - 4a\ **c**\)/2a
    :return:
    """
    _LAB_2C_SQRT = math.sqrt(x + y)
    _LAB_2C_QUADRATIC = -b + math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    _LAB_2C_EXPONENT = x ** (y + 7)
    if x == 10 and y == 6 and a == 2 and b == 8 and c == 1:
        print(
            f'\033[4mLab2C with default values: x = {x}, y = {y}, a = {a}, b = {b}, c = {c}.\033[0m')
    else:
        print(
            f'\033[4mLab2C with custom values: x = {x}, y = {y}, a = {a}, b = {b}, c = {c}.\033[0m')
    print("For x =", x, ", y =", y, ". The square root of x + y =", _LAB_2C_SQRT,  # normal format
          "or %.2f" % _LAB_2C_SQRT)  # %f format
    print("For a =", a, ", b =", b, ", c =", c,
          ". The quadratic formula for (-b + sqrt(b^2 - 4ac)/2a =", _LAB_2C_QUADRATIC,
          "or %-10f" % _LAB_2C_QUADRATIC,  # %f format but with left-justify and without .2f to show un-rounded value
          "or", f'{_LAB_2C_QUADRATIC:.2f}')  # f-string format
    print("For x =", x, ", y =", y, ". The formula x ^ (y + 7) =", f'{_LAB_2C_EXPONENT:,}')  # f-string format
    print("-" * 50)


lab_2_heading(letter="C")
lab_2c_print()
lab_2c_print(2, 10, 10, 20, 4)
print(lab_2c_print.__doc__)
# =============================================================================
# LAB 2D
# =============================================================================


def lab_2d_print(middleName: bool = False):
    r"""
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
    :param middleName: Boolean; default is False; True to enable input of middle name
    :return: None
    """
    firstName = str(input("Please enter your first name in using lowercase letters: "))
    print(firstName.isalpha())
    while firstName.islower() is False or firstName.isalpha() is False:  # OR conditional to check format
        print("Your first name was entered as %s. This format is not in lowercase or is a number" % firstName)
        firstName = input("Please enter your first name in using lowercase letters: ")
    if middleName:  # optional function parameter to enable middle name input, default is middleName=False
        middleName = input("Please enter your middle name in using lowercase letters: ")
        while middleName.islower() is False or middleName.isalpha() is False:
            print("Your middle name was entered as %s. This format is not in lowercase or is a number" % middleName)
            middleName = input("Please enter your middle name in using lowercase letters: ")
    lastName = input("Please enter your last name in using lowercase letters: ")
    while lastName.islower() is False or lastName.isalpha() is False:
        print("Your last name was entered as %s. This format is not in lowercase or is a number" % lastName)
        lastName = input("Please enter your last name in using lowercase letters: ")
    try:
        fullName = "%s %s %s" % (firstName.title(), middleName.title(), lastName.title())
        initials = "%s %s %s" % (firstName[0].upper(), middleName[0].upper(), lastName[0].upper())
    except AttributeError:
        fullName = "%s %s" % (firstName.title(), lastName.title())
        initials = "%s %s" % (firstName[0].upper(), lastName[0].upper())
        # initials = "{0}{1}".format(firstName[0].upper(), lastName[0].upper())  #using .format instead of %s specifier
    while True:
        try:  # allows input of invalid age in string format without crashing due to value error, loop until valid value
            ageString = input("Please enter your age: ")  # allows invalid value to be shown in ValueError print stmt
            age = int(ageString)
            if isinstance(age, int):  # break loop only if variable age is an integer
                break
        except ValueError:
            print("Your age was entered as %s. This format is not an integer" % ageString)
    print("*" * 50)
    print("%25s" % fullName.title())
    print(fullName.upper())
    print("%s" % initials)
    print("The length of my name is %s letters (without spaces) and %s letters with spaces"
          % (len(fullName.replace(" ", "")), len(fullName)))  # 2nd line due to PEP8 over character limit
    # print(f'The length of my full name is {len(fullName)}')  # length of name in f-string format
    print("%sers" % 49)
    # print("{0}ers".format(49))  # using .format instead of %s specifier
    print("My age in 10 years is %s" % (age + 10))
    if age > 122:
        print("Your age is %s. Are you are a vampire?" % age)
    print(" " * 50 + "'s")


lab_2_heading(letter="D")
lab_2d_print()
print("-" * 50)
print(lab_2d_print.__doc__)
# =============================================================================
# LAB 2E
# =============================================================================


def lab_2e_print(phoneNumber=0000000000):
    r"""
    The following pseudocode describes how to turn a string containing a ten-digit phone number (such as "4155551212")
    into a more readable string with parentheses and dashes, like this: "(415) 555-1212".
    “Take the string consisting of the first three characters and concat with "(" and ") ". This is the area code.

    Concatenate the area code, the string consisting of the next three characters, a hyphen, and the string
    consisting of the last four characters. This is the formatted number.”

    Sample Output:
    The phone number is: 8884554415
    The formatted number is: (888) 455-4415
    :param phoneNumber: lab_2e_print(phoneNumber=\ **phoneNumber(int)**\)
    :return: None
    """
    phoneNumber = "%09.f" % phoneNumber
    phoneNumberFormatted = "(" + phoneNumber[:3] + ") " + phoneNumber[3:6] + "-" + phoneNumber[-4:]
    # start at array[0] to before array[3], start at array[3] to before array[6], start at array[len(variable) -4 = 9-4]
    # phoneNumberFormatted = f'({phoneNumber[:3]}) {phoneNumber[3:6]}-{phoneNumber[6:]}'  # f-string code
    print("The phone number is: " + phoneNumber)
    print("The formatted number is: " + phoneNumberFormatted)
    print("-" * 50)


lab_2_heading(letter="E")
lab_2e_print()
lab_2e_print(phoneNumber=884554415)
print(lab_2e_print.__doc__)
