#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Lab 1a
'''Implement the following program in your IDE.'''
##
# Sample program that demonstrates the print function
#

# Prints 7
print (3+4)

# Prints "Hello World!" in two lines.
print("Hello")
print("World!")

# Prints multiple values with a single print function call
print("My favorite numbers are", 3 + 4, "and", 3 + 10)

#Prints three lines of text with a blank line.
print("Goodbye")
print()
print("Home to see you again")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Lab 1b
'''Implement the code then fix the errors (2 syntax, 1 logical) so that the program produces the following output:'''
print("The itsy bitsy spider climbed up the waterspout")
print("Down came the rain")
print("and washed the spider out")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Lab 1c
'''Write an algorithm that finds and prints the largest number from among 15 non-negative numbers entered by the user. Rearrange the following lines to produce the algorithm that accomplished this task.'''
'''
Repeat 15 times:
If userNum > largestNum: done
Prompt user for next number done
largestNum = 0 done
largestNum = userNum done
Print largestNum
userNum = Input number from user done
'''
#Rearranged:
'''
largestNum = 0
userNum = Input number from user
If userNum > largestNum:
largestNum = userNum
Print largestNum
Prompt user for next number
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Lab 1d
'''
Problem Statement:
You have the choice of buying two cars. One is more fuel efficient than the other, but also more expensive.
You know the price and fuel efficiency (in miles per gallon, mpg) of both cars.
You plan to keep the car for ten years.
Which car is the better deal?
Work with a partner to write this algorithm.
'''

PURCHASE_PRICE_NOT_EFFICENT = 10000
PURCHASE_PRICE_EFFICIENT = 20000
MILES_PER_YEAR = 15000
years = 10
TOTAL_MILES = MILES_PER_YEAR * years
pricePerGallon = 4.617
mpgNotEfficient = 20
mpgEfficient = 30

priceNotFuelEfficient = PURCHASE_PRICE_NOT_EFFICENT + (TOTAL_MILES / mpgNotEfficient) * pricePerGallon
priceFuelEfficient = PURCHASE_PRICE_EFFICIENT + (TOTAL_MILES / mpgEfficient) * pricePerGallon
print("The price of a not-fuel-efficient car is $", "{:.2f}".format(priceNotFuelEfficient))
print("The price of a fuel-efficient car is $", "{:.2f}".format(priceFuelEfficient))