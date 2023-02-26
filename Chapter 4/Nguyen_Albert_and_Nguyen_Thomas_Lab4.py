# Due to PEP8, 2 blank lines at start and end of functions in labs below, also variable in functions in camelCase
# Lab 4a


def print_multiples_of_5_10(n):  # parameter1 is passing argument from variable n in outer scope
    numberToTest = 1  # numberToTest starts at 1 to exclude negative numbers and 0
    print("Printing all multiples of 5 or 10 less than %d:" % n)
    while numberToTest < n:
        if numberToTest % 5 == 0 or numberToTest % 10 == 0:  # check if numberToTest is multiple of 5 or 10
            print(numberToTest)
        numberToTest = numberToTest + 1  # or numberToTest += 1, go to next array: numberToTest[0]=>[1]=>[2]=>[n-1]<n
    return numberToTest  # return value won't be printed


n = 20  # variable n or given number is the upper limit which loop stops at once while loop increment finishes
print_multiples_of_5_10(n)  # With n = 20
print_multiples_of_5_10(30)  # With n = 30


# Lab 4b


def vowel_count(string):  # to keep vowelCounter and stringArrayNum local, default para is string
    vowelCounter = 0  # start at count 0
    stringArrayNum = 0  # start at string[0][Array=0]
    vowels = "aeiouAEIOU"
    while stringArrayNum < len(string):  # the length of the string, i.e. len("foo") = 3, loop foo[0],foo[1],foo[2]
        if string[stringArrayNum] in vowels:  # i.e. vowelCounter = 0, foo[0] = f, foo[1] = o, vowelCounter += 1
            vowelCounter = vowelCounter + 1  # or vowelCounter += 1, add to
        # or stringArrayNum += 1: after executing if statement(vowelCounter), look at next stringArray[0] => [1] => [2]
        stringArrayNum = stringArrayNum + 1
        # print statement commented out in function to practice assigning function to return values:
        # print("The string \"%s\" has %d vowels." % (parameter1, vowelCounter))  # commented out
    return vowelCounter  # return the vowel count to be assigned outside function


# Default, i.e. string = input("Albert-o")
string = input("Enter a string: ")
vowelCounter = vowel_count(string)  # call function on string and assign vowel counter to function output, default para
print("The string \"%s\" has %d vowels." % (string, vowelCounter))  # format vowelCounter with integer %d specifier

# Bypassing the input() function with string = "Thomas"
string = "Thomas"
vowelCounter = vowel_count(string)  # call function, must explicitly pass variable "string" as parameter
print(f"The string \"{string}\" has {vowelCounter} vowels.")  # using f string, \ to escape the double quotes

# Lab 4c
grades = []
grade = 0
passing_grades = 0
failing_grades = 0
sum_of_grades = 0

while grade != -1:
    grade = float(input("Enter a grade or -1 to finish: "))
    if grade != -1:
        grades.append(grade)
        sum_of_grades += grade
        if grade >= 60:
            passing_grades += 1
        else:
            failing_grades += 1

if len(grades) == 0:
    print("No grades were entered.")
else:
    avg_grade = sum_of_grades / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)

    print(f"The average grade is {avg_grade:.2f}")
    print(f"Number of passing grades is {passing_grades}")
    print(f"Number of failing grades is {failing_grades}")
    print(f"The maximum grade is {max_grade:.2f}")
    print(f"The minimum grade is {min_grade:.2f}")


# Lab 4d


def compound_interest(numYears):  # calculate and print balance for each year
    INTEREST_RATE = 0.05
    INITIAL_BALANCE = 10000.00
    print("For Initial Balance of $%10.2f at %.2f%%, for %d years, the balance of each year is as follows: "
          % (INITIAL_BALANCE, INTEREST_RATE * 100, numYears))  # multi-line print statement due to line length
    balance = INITIAL_BALANCE  #
    currentYear = 0
    while currentYear < numYears:  #
        balance = balance + balance * INTEREST_RATE
        currentYear = currentYear + 1  # start printing at year 1
        print("For Year: %4d, Balance is $%10.2f" % (currentYear, balance))  # print balance for each year
    print("*" * 30)  # Seperator between function calls
    # Using For loop:
    # for currentYear in range(1, numYears + 1):
    #     balance = balance + balance * INTEREST_RATE
    #     print("For Year: %4d, Balance is $%10.2f" % (currentYear, balance))


numYears = int(input("Enter number of years: "))
compound_interest(numYears)  # Using input(), example: 5 years
compound_interest(2)  # 2 years

# Lab 4e
# Nested loop to print three rows and four columns of brackets
for i in range(3):
    for j in range(4):
        print("[]", end="")
    print()  # Start a new line after each row

# Lab 4f
n = int(input("Enter n: "))

# Print the header
print("   |", end="")
for i in range(1, n + 1):
    print("{0:5d}".format(i), end="")
print()

# Print the separator
print("-------------------------------")

# Print the table
for i in range(1, n + 1):
    print("{0:3d}|".format(i), end="")
    for j in range(1, n + 1):
        print("{0:5d}".format(i * j), end="")
    print()

# Lab 4g
string = input("Enter a string: ")

lowercase_count = 0
uppercase_count = 0
digit_count = 0
symbol_count = 0

for char in string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print(f"Total counts of Chars = {lowercase_count + uppercase_count}")
print(f"Total counts of Digits = {digit_count}")
print(f"Total counts of Symbol = {symbol_count}")

# Lab 4h
from random import randint  # import statement usually at top, import only randint module from random


def roll_dice(numRolls=10):  # default 10 rolls
    print("The dice is rolled %d times" % numRolls)
    for roll in range(numRolls):  # start at roll[0] increment by 1,... range function stops at position numRolls[]
        dieOne = randint(1, 6)  # random integer between 1 and 6
        dieTwo = randint(1, 6)
        print(dieOne, dieTwo)
    return dieOne, dieTwo  # return valley won't be printed, example of returning 2 values


roll_dice()
roll_dice(5)  # 5 rolls
