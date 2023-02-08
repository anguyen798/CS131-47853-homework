# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lab 1a
"""Implement the following program in your IDE."""
##
# Sample program that demonstrates the print function
#

# Prints 7
print(3 + 4)

# Prints "Hello World!" in two lines.
print("Hello")
print("World!")

# Prints multiple values with a single print function call
print("My favorite numbers are", 3 + 4, "and", 3 + 10)

# Prints three lines of text with a blank line.
print("Goodbye")
print()
print("Home to see you again")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lab 1b
'''Implement the code then fix the errors (2 syntax, 1 logical) so that the program produces the following output:'''
print("The itsy bitsy spider climbed up the waterspout")
print("Down came the rain")
print("and washed the spider out")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lab 1c
'''
Write an algorithm that finds and prints the largest number from among 15 non-negative numbers entered by the user.
Rearrange the following lines to produce the algorithm that accomplished this task.
'''

'''
Repeat 15 times:
If userNum > largestNum:
Prompt user for next number
largestNum = 0
largestNum = userNum
Print largestNum
userNum = Input number from user
'''
# Rearranged:
'''
largestNum = 0
userNum = Input number from user
If userNum > largestNum:
largestNum = userNum
Print largestNum
Prompt user for next number
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lab 1d
'''
Problem Statement:
You have the choice of buying two cars. One is more fuel efficient than the other, but also more expensive.
You know the price and fuel efficiency (in miles per gallon, mpg) of both cars.
You plan to keep the car for ten years.
Which car is the better deal?
Work with a partner to write this algorithm.
'''
# default CONSTANTS and variables for 1d, variables changeable if manual_variables_1d=True
MILES_PER_YEAR = 15000
YEARS = 10
TOTAL_MILES = MILES_PER_YEAR * YEARS

price_vehicle_nonefficient = 10000
price_vehicle_efficient = 20000
mpg_non_efficient = 20
mpg_efficient = 30
price_per_gallon = 1.999

# Manual variable condition, else use default values above, convert text input() to float
manual_variables_1d = False  # change variable to True to enter values manually
if manual_variables_1d:
    price_vehicle_nonefficient = float(input("Price of non-fuel efficient vehicle"))
    price_vehicle_efficient = float(input("Price of fuel efficient vehicle"))
    mpg_non_efficient = float(input("Miles/Gallon of non-fuel efficient vehicle"))
    mpg_efficient = float(input("Miles/Gallon of fuel efficient vehicle"))
    price_per_gallon = float(input("Price/Gallon"))

# Assign and print price of vehicles
priceNotFuelEfficient = price_vehicle_nonefficient + (TOTAL_MILES / mpg_non_efficient) * price_per_gallon
priceFuelEfficient = price_vehicle_efficient + (TOTAL_MILES / mpg_efficient) * price_per_gallon
# priceNotFuelEfficient = priceFuelEfficient  # Scenario where the prices for vehicles are equal
print("The price of a non fuel efficient vehicle is $", f'{priceNotFuelEfficient:,.2f}.')
print("The price of a fuel efficient vehicle is $", f'{priceFuelEfficient:,.2f}.')

# Print which vehicle is better deal
if priceNotFuelEfficient > priceFuelEfficient:
    print("The fuel efficient vehicle is the better deal than the non fuel efficient vehicle.")
elif priceNotFuelEfficient < priceFuelEfficient:
    print("The non fuel efficient vehicle is the better deal than the fuel efficient vehicle.")
else:
    print("The fuel efficient vehicle and non fuel efficient vehicle value are equal at this mpg and purchase price")
