#Initialize variables to mantain the running total and count
total = 0.0  # Outside the while loop: declare and initialize variables to use
count = 0

salary = 0.0
while salary >= 0.0:  # Since salary is initialized to 0, the while loop statements will execute at least once
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0 :  #
        total = total + salary
        count = count + 1

#Compute and print the average salary.
if count > 0:  # Prevent divide by 0
    average = total / count
    print("Average salary is", average)
else:
    print("No data was entered.")