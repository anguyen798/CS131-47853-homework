filename = input("Enter the input filename: ")
with open(filename, 'r') as file :
    columnOneSum = 0.0
    columnTwoSum = 0.0
    n = 0
    for line in file :
        columnOne, columnTwo = line.split()
        columnOneSum = columnOneSum + float(columnOne)
        columnTwoSum = columnTwoSum + float(columnTwo)
        n = n + 1

columnOneAverage = columnOneSum / n
columnTwoAverage = columnTwoSum / n

print("The averages are %.2f and %.2f" % (columnOneAverage, columnTwoAverage))