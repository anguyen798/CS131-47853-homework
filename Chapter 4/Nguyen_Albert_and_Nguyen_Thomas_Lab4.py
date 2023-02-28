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
def grades_compute():
    # Set all starting values to empty list or 0
    grades = []
    grade = 0
    passing_grades = 0
    failing_grades = 0
    sum_of_grades = 0

    while grade != -1:
        grade = float(input("Enter a grade or -1 to finish: "))  # -1 is sentinel to end while loop
        if grade != -1:
            grades.append(grade)  # .append method to add grade to the grades list
            sum_of_grades = sum_of_grades + grade
            if grade >= 60:
                passing_grades = passing_grades + 1
            else:
                failing_grades = failing_grades + 1

    if len(grades) == 0:  # if condition to show no grades were entered
        print("No grades were entered.")
    else:
        avg_grade = sum_of_grades / len(grades)  # find the average of grades list
        max_grade = max(grades)  # find min value in grades list
        min_grade = min(grades)  # find max value in grades list

        print("The average grade is %.2f" % avg_grade)
        print("Number of passing grades is %d" % passing_grades)
        print("Number of failing grades is %d" % failing_grades)
        print("The maximum grade is %.2f" % max_grade)
        print("The minimum grade is %.2f" % min_grade)


grades_compute()


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
def bracket_print(rows=3, columns=4):  # keyword parameter, default rows = 3 and columns = 4
    print("Printing %d rows and %d columns" % (rows, columns))
    for row in range(rows):  # Range function no start parameter=start[0], stop at row 3 (array[3])
        for column in range(columns):  # Outer-row-loop only runs after nested-column-loop completes
            print("[]", end="")  # Print brackets on one row, parameter end="" instead of newline "\n" after every print
        print()  # Go to next row after nested-column-loop runs and brackets are all finished printing on same row
        # Then continue outer row for loop - print statement will execute at end of every interation of outer-row-loop


bracket_print()  # Using default parameter values: 3 rows, 4 columns
bracket_print(6, 2)  # Custom parameter value: 6 rows, 2 columns


# Lab 4f
def multiplication_table(n):
    print("-----" + "-" * 5 * n)  # Print dash seperator: 5 dashes and 5 dashes for each n
    print("For a multiplication table of %d numbers:" % n)  # Description of how many numbers to multiply
    print(" " * 2 + "|", end="")  # Print header row without newline, Start at 3 spaces, then run loop print on same row
    for column_number_header in range(1, n + 1):  # Start at 1 (array[0]) and stop before number+1, n (array[n+1])
        print("%5d" % column_number_header, end="")  # Pad 5 spaces between each number, after each print no newline
    print()  # After for loop, print new row
    print("-----" + "-" * 5 * n)  # Print dash seperator: 5 dashes and 5 dashes for each n
    for row_number_header in range(1, n + 1):  # Print table: for loop = row header, nested for loop = multiplied values
        print("%3d" % row_number_header, end="")  # Pad 3 spaces to start the row header then run
        for multiplier in range(1, n + 1):  # Before each row header is created, nested-for-loop values on same line
            print("%5d" % (row_number_header * multiplier), end="")  # Pad 5 spaces between each multiplied value
        print()  # After nested-for-loop prints on same line, start a new row


n = int(input("Enter n: "))  # Using input, example: Multiplication table of 10 values, variable n shared with 4a
multiplication_table(n)
multiplication_table(5)  # Multiplication table of 5 values


# Lab 4g
def string_counter(string):
    print("-" * 30)  # Header seperator print statement
    print("Below are the character counts for the string %s:" % string)  # Description of string for function calls
    # Set all count starting values to 0
    letter_count = 0
    digit_count = 0
    symbol_count = 0

    for character in string:  # start with string[0] then end at string[len(string)]
        if character.isalpha():  #
            letter_count = letter_count + 1
        elif character.isdigit():
            digit_count = digit_count + 1
        else:  # for characters that aren't letters or numbers such as !@#$%^&*()-_=+[{]}\|`~,<.>/?,...
            symbol_count = symbol_count + 1

    print("Total counts of Chars = %d" % letter_count)  # Chars stand for letters
    print("Total counts of Digits = %d" % digit_count)
    print("Total counts of Symbol = %d" % symbol_count)


string = input("Enter a string: ")  # input(), example: string="Thomas1337"
string_counter(string)
string_counter("Anguyen798")

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
