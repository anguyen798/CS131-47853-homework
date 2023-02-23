rate5.0
INITIAL_BALANCE = 10000.0
TARGET = 2 * INITIAL_BALANCE

balance = INITIAL_BALANCE
year = 0

while balance < TARGET :
    year = year + 1
    interest = balance * rate / 100
    balance = balance + interest

print("The investment doubled after", year, "years.")