# Lab 4a
n = 34
i = 1
while i < n:
    if i % 5 == 0 or i % 10 == 0:
        print(i)
    i += 1

# Lab 4b
string = input("Enter a string: ")
def vowel_count(para1=string):
    vowelCounter = 0
    stringArrayNum = 0
    vowels = "aeiouAEIOU"
    while stringArrayNum < len(string):
        if string[stringArrayNum] in vowels:
            vowelCounter += 1
        stringArrayNum += 1
    print("The string has %s vowels." % vowelCounter)
vowel_count(string)

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
# Constants
INTEREST_RATE = 0.05
INITIAL_BALANCE = 10000.00

# Prompt user for number of years
numYears = int(input("Enter number of years: "))

# Calculate and display incrementing balance for each year
balance = INITIAL_BALANCE
for year in range(1, numYears + 1):
    balance += balance * INTEREST_RATE
    print("Year: {:4} Balance: {:10.2f}".format(year, balance))


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
for i in range(1, n+1):
    print("{0:5d}".format(i), end="")
print()

# Print the separator
print("-------------------------------")

# Print the table
for i in range(1, n+1):
    print("{0:3d}|".format(i), end="")
    for j in range(1, n+1):
        print("{0:5d}".format(i*j), end="")
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

print(f"Total counts of Chars = {lowercase_count+uppercase_count}")
print(f"Total counts of Digits = {digit_count}")
print(f"Total counts of Symbol = {symbol_count}")

# Lab 4h
import random

for i in range(10):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(die1, die2)
