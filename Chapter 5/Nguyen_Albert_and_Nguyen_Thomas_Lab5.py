# Header Function
def header_function(letter):
    print("*" * 50)
    print("Lab 5%s" % letter)
    print("*" * 50)


# Lab 5b
def volume_rectangle(length, width, height) :
    print("Enter the length: %d" % length)  # emulate input()
    print("Enter the width: %d" % width)
    print("Enter the height: %d" % height)
    volume = length * width * height
    print("A rectangular prism with dimensions %d, %d, %d has a volume of %d"
          % (length, width, height, volume))


# Header seperator
header_function("b")
# Function call
volume_rectangle(3,4,2)
