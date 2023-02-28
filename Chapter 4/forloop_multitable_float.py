rows = int(input("Enter the total rows here: "))
columns = rows  # when number of rows = number of columns
column_multiplier = 1.37
print("For a row with %d rows and %d columns" % (rows, columns))
# Print header row
print(" " * 7, end="")  # 5 blank space for row headers
for column_header in range(1, columns+1):
    print("%7.2f" % (column_header * column_multiplier), end="")
print()
print(" " * 7 + "-" * 7 * columns)
for row_header in range(1,rows+1):  # 1 to 5, row # print multi-table
    print("%7.2f" % row_header, end="") # row header
    for multiplier in range (1,columns+1):
        print("%7.2f" % (row_header * (multiplier * column_multiplier)), end="")  # column with 5 spaces between, same line
    print()  # blank line for next row
